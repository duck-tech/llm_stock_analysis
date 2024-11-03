from crewai import Task 
from textwrap import dedent


class AnalysisTasks:

    def research(self, agent, company):
        return Task(
            description=dedent(
                f"""
                正在搜索並總結最新的{company}公司動態與新聞。
                特別關注最近發生的重大事件。
                """
            ),
            agent=agent,
            expected_output="用列表的形式總結頭5項最重要的公司新聞"
        )