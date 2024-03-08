import subprocess
import requests
import json
from http import HTTPStatus
import panel as pn
import os
import requests
import re
# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus

url = "https://api.baichuan-ai.com/v1/chat/completions"

api_key = "your_api_key"

headers = {
    "Content-Type": "application/json",
    "Authorization":f"Bearer {api_key}"
}

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
    data = {
        "model": "Baichuan2-Turbo",
        "messages": messages,
        "stream": False,
        "temperature": 0,
        "top_p": 0.85,
        "top_k": 5,
        "with_search_enhance": False
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = json.loads(response.text)
        res = result['choices'][0]['message']['content']

    return res

response = get_completion_from_messages(messages)
print(response)