import requests
import json
import os 
from langchain.tools import tool

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class SearchTools: 
    
    @tool
    def searchInfo(query:str):
        """在網上搜索關於指定內容的相關資訊"""

        return SearchTools.search(query)
    
    def search(query:str):
        url = "https://google.serper.dev/news"

        payload = json.dumps({
        "q": query,
        "hl": "zh-tw"
        })
        headers = {
        'X-API-KEY': os.environ["SERPER_API_KEY"],
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        news = response.json()["news"]

        string = []
        for new in news:
            try:
                string.append("\n".join([
                    f"標題: {new['title']}",
                    f"時間: {new['data']}",
                    f"來源: {new['source']}"
                    f"內容摘要: {new['snippet']}"
                ]
                ))
            except KeyError:
                next
        content = '\n'.join(string)
        return f"\n搜索結果是: {content}\n"