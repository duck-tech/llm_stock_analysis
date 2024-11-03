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
        try: 
            response = requests.request("POST", url, headers=headers, data=payload)
            response.raise_for_status()
            results = response.json()['news']
        except requests.exceptions.RequestException as e:
            print(f"搜索請求失敗: {str(e)}")
            return "搜索失敗，請稍後重試"
        

        string = []
        for result in results:
            try:
                string.append('\n'.join([
                    f"標題: {result['title']}",
                    f"時間: {result['date']}",
                    f"來源: {result['source']}",
                    f"摘要: {result['snippet']}", "\n-----------------"
                ]))
            except KeyError:
                next

        content = '\n'.join(string)
        return f"\n Search result: {content}\n"