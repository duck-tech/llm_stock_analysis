from crewai import Agent
from tools.search import SearchTools

class AnalysisAgents:
    def __init__(self, llm):
        self.llm = llm

    def market_research_analyst(self):
        return Agent(
            role="市場研究分析師",
            goal="搜索並分析公司的市場表現和財務狀況，整理出重要信息",
            backstory="""你是一位經驗豐富的市場研究分析師，專長於：
            1. 快速掌握市場動態
            2. 準確解讀財務數據
            3. 洞察行業趨勢
            4. 發現潛在投資機會
            請用中文思考和溝通。""",
            llm=self.llm,
            tools=[SearchTools.searchInfo],
            allow_delegation=False, #是否允許任務交給其他人完成
            max_iter=3,
            verbose=True
        )
    
    def cfa(self):
        return Agent(
            llm=self.llm,
            role="特許財務分析師",
            goal="根據市場研究報告進行深入分析，提供專業的投資建議",
            backstory="""你是一位資深的特許財務分析師，專長於：
            1. 深度財務分析
            2. 價值投資評估
            3. 風險管理
            4. 投資組合規劃
            請用繁體中文思考和溝通。""",
            allow_delegation=False,
            verbose=True
        )