from crewai import Crew, Process
from langchain.llms import Ollama
from agents import AnalysisAgents
from tasks import AnalysisTasks
import sys

class FinancialCrew:
    def __init__(self, company: str):
        self.company = company
        try:
            self.llm = Ollama(model="llama3:latest")  
        except Exception as e:
            print(f"初始化 LLM 失敗: {str(e)}")
            sys.exit(1)

    def run(self):
        try:
            agents = AnalysisAgents(self.llm)
            tasks = AnalysisTasks()

            mr_analyst = agents.market_research_analyst()
            cfa = agents.cfa()

            research = tasks.research(mr_analyst, self.company)
            analysis = tasks.analysis(cfa, research)

            crew = Crew(
                agents=[mr_analyst, cfa],
                tasks=[research, analysis],
                process=Process.sequential,
                verbose=True
            )

            result = crew.kickoff()
            return result

        except Exception as e:
            print(f"分析過程發生錯誤: {str(e)}")
            return None

if __name__ == "__main__":
    print("\n\n## 歡迎來到AI投資顧問團隊")
    print("-----------------------")
    
    try:
        company = input("\n請輸入想分析的公司名稱\n")
        financial_crew = FinancialCrew(company)
        result = financial_crew.run()
        
        if result:
            print("\n\n#########################")
            print("## 分析結果")
            print("#######################\n")
            print(result)
        else:
            print("\n分析未能完成，請稍後重試")
            
    except KeyboardInterrupt:
        print("\n\n程序已終止")
    except Exception as e:
        print(f"\n發生未預期的錯誤: {str(e)}")