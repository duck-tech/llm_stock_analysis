from crewai import Task 
from textwrap import dedent


class AnalysisTasks():

    def research(self, agent, company):
        return Task(
            description=dedent(
                f"""
                搜索並總結最新的公司動態與新聞。
                特別關注重大事件。
                搜索的公司是{company}"""
            ),
            agent=agent,
            expected_output="用列表的形式總結頭五項最重要的公司新聞"
        )