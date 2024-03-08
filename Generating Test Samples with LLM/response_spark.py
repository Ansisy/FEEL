import os
import re
from sparkapi.core.api import SparkAPI
from sparkapi.core.config import SparkConfig
import json

os.environ['SPARK_APP_ID'] = "your_app_id"  
os.environ['SPARK_API_SECRET'] = "your_spi_secret" 
os.environ['SPARK_API_KEY'] = "your_api_key"  
os.environ['SPARK_API_MODEL'] = "v3.0"  
os.environ['SPARK_CHAT_MAX_TOKENS'] = "20000"
os.environ['SPARK_CHAT_TEMPERATURE'] = "0"
os.environ['SPARK_CHAT_TOP_K'] = "4"
config = SparkConfig().model_dump()  
api = SparkAPI(**config)

# get completion from messages
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

res = api.get_completion_from_messages(messages)
ans = ''.join(res)
print(ans)

