from http import HTTPStatus
from dashscope import Generation
import dashscope
from dashscope.api_entities.dashscope_response import Role
import panel as pn
import os
import requests
import re
# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope

dashscope.api_key='your_api_key' 

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

def get_completion_from_messages(messages):
    gen = Generation()
    response = gen.call(
        Generation.Models.qwen_turbo,
        messages=messages,
        result_format='message',  
    )
    if response.status_code == HTTPStatus.OK:
        print(response.output.choices[0]['message']['content'])
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))

    return response.output.choices[0]['message']['content']

res = get_completion_from_messages(messages)

