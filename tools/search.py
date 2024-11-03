import requests
import json
import os 
from langchain.tools import tool


class SearchTools: 
    
    @tool("搜索網上相關資訊")
    def searchInfo(query:str):
        """在網上搜索關於指定內容的相關資訊"""

        return SearchTools.search(query)
    
    def search(query:str):
        url = "https://google.serper.dev/news"

        payload = json.dumps({
        "q": "apple inc",
        "hl": "zh-tw"
        })
        headers = {
        'X-API-KEY': os.environ["SERPER_API_KEY"],
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)