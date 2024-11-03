from crewai import Crew, Process
from langchain.llms import Ollama

from agents import AnalysisAgents
from tasks import AnalysisTasks

llm = Ollama(model="llama3.2:latest")


class FinicialCrew:

    def __init__(self,company:str):
        self.company = company 
    
    def run(self):

        agents = AnalysisAgents(llm)
        tasks = AnalysisTasks()

        mr_analyst = agents.market_research_analyst()
        cfa = agents.cfa()

        research = tasks.research(mr_analyst, self.company)

        crew = Crew(
            agents = [mr_analyst, cfa],
            tasks = [research],
            process = Process.sequential,
            verbose = True
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("\n\n## 歡迎來到AI投資顧問團隊")
    print("-----------------------")
    company = input("\n請輸入想分析的公司名稱\n")

    financial_crew = FinicialCrew(company)
    result = financial_crew.run()
    print("\n\n#########################")
    print("## 如下是分析結果")
    print("#######################\n")
    print(result)