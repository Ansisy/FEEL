import json
import re
import numpy as np
import panel as pn
from colorama import init, Fore
from loguru import logger
from openai import OpenAI

from tool_register import get_tools, dispatch_tool

init(autoreset=True)

client = OpenAI(
    api_key="your_api_key",
    base_url="chatglm_url",
)

messages = [
    {'role': 'user', 'content': """
You are a  person skilled in the theory of emotional support.
Please make your response in English and limit your response to 30 words, it is very important! Also this reply should be complete, not half spoken.
What you need to do is give your emotionally supportive responses based on this set of conversations above:
{
     
        [Dialog data here]

}
Now,you need to response to this sentence:["usr", "Target sentence here"]}
  """},
]

functions = list(get_tools().values())


def run_conversation(query: str, stream=False, functions=None, max_tries=5):
    params = dict(model="chatglm3", messages=messages, stream=stream)
    if functions:
        params["functions"] = functions
    response = client.chat.completions.create(**params)

    output = "" 

    for _ in range(max_tries):
        if not stream:
            if response.choices[0].message.function_call:
                function_call = response.choices[0].message.function_call
                logger.info(f"Function Call Response: {function_call.model_dump()}")

                function_args = json.loads(function_call.arguments)
                tool_response = dispatch_tool(function_call.name, function_args)
                logger.info(f"Tool Call Response: {tool_response}")

                params["messages"].append(
                    response.choices[0].message.model_dump(include={"role", "content", "function_call"}))
                params["messages"].append(
                    {
                        "role": "function",
                        "name": function_call.name,
                        "content": tool_response 
                    }
                )
            else:
                reply = response.choices[0].message.content
                logger.info(f"Final Reply: \n{reply}")
                return reply 

        else:
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                if isinstance(content, str):  
                    print(Fore.BLUE + content, end="", flush=True)
                    output += content

                if chunk.choices[0].finish_reason == "stop":
                    return output 

                elif chunk.choices[0].finish_reason == "function_call":
                    print("\n")

                    function_call = chunk.choices[0].delta.function_call
                    logger.info(f"Function Call Response: {function_call.model_dump()}")

                    function_args = json.loads(function_call.arguments)
                    tool_response = dispatch_tool(function_call.name, function_args)
                    logger.info(f"Tool Call Response: {tool_response}")

                    params["messages"].append(
                        {
                            "role": "assistant",
                            "function_call": function_call,
                            "content": output
                        }
                    )
                    params["messages"].append(
                        {
                            "role": "function",
                            "name": function_call.name,
                            "content": tool_response
                        }
                    )

                    break

        response = client.chat.completions.create(**params)


def run_conversation_v2(query: str, stream=False, tools=None, max_tries=5):
    params = dict(model="chatglm3", messages=messages, stream=stream)
    if tools:
        params["tools"] = tools
    response = client.chat.completions.create(**params)

    for _ in range(max_tries):
        if not stream:
            if response.choices[0].message.tool_calls:
                function_call = response.choices[0].message.tool_calls[0]
                logger.info(f"Function Call Response: {function_call.model_dump()}")

                function_args = json.loads(function_call.function.arguments)
                tool_response = dispatch_tool(function_call.function.name, function_args)
                logger.info(f"Tool Call Response: {tool_response}")

                params["messages"].append(
                    response.choices[0].message.model_dump(include={"role", "content", "tool_calls"})
                )
                params["messages"].append(
                    {
                        "role": "tool",
                        "tool_call_id": "random",
                        "content": tool_response,  
                    }
                )
            else:
                reply = response.choices[0].message.content
                logger.info(f"Final Reply: \n{reply}")
                return

        else:
            output = ""
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(Fore.BLUE + content, end="", flush=True)
                output += content

                if chunk.choices[0].finish_reason == "stop":
                    return

                elif chunk.choices[0].finish_reason == "function_call":
                    print("\n")

                    function_call = chunk.choices[0].delta.tool_calls[0]
                    logger.info(f"Function Call Response: {function_call.model_dump()}")

                    function_args = json.loads(function_call.function.arguments)
                    tool_response = dispatch_tool(function_call.function.name, function_args)
                    logger.info(f"Tool Call Response: {tool_response}")

                    params["messages"].append(
                        {
                            "role": "assistant",
                            "tools_call": [function_call.model_dump()],
                            "content": output
                        }
                    )
                    params["messages"].append(
                        {
                            "role": "tool",
                            "tool_call_id": "random",
                            "content": tool_response, 
                        }
                    )

                    break

        response = client.chat.completions.create(**params)


response = run_conversation(messages, functions=functions, stream=False)

