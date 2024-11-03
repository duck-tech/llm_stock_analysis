from crewai import Task 
from textwrap import dedent


class AnalysisTasks:

    def research(self, agent, company):
        return Task(
            description=dedent(
                f"""
                 請執行以下任務：
                1. 搜索並整理{company}公司最新的新聞和市場動態
                2. 特別關注以下方面：
                   - 公司最近的重大事件
                   - 財務表現
                   - 市場地位變化
                   - 產品或服務更新
                   - 產業環境變化
                3. 將搜索到的信息進行分類整理
                4. 按重要性排序，提取最關鍵的信息

                請用列表形式列出5個最重要的發現，每個發現需要包含：
                - 事件描述
                - 發生時間
                - 潛在影響
                """
            ),
            async_execution=True,
            agent=agent,
        )
    def analysis(self, agent, context):
        return Task(
            description=dedent(
                f"""
                基於前面搜索到的信息，請完成以下分析任務：
                1. 公司綜合分析
                   - 業務發展現況
                   - 財務健康度
                   - 市場競爭力
                   - 未來發展潛力
                
                2. 風險評估
                   - 內部風險因素
                   - 外部市場風險
                   - 產業風險
                
                3. 投資建議
                   - 股票投資價值評估
                   - 建議操作方向（買入/持有/賣出）
                   - 投資風險提醒

                請提供一份結構化的分析報告，用繁體中文描述, 包含上述所有要點。
                """
            ),
            agent=agent,
            context = [context],
        )