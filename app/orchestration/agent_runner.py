from app.agents.planner_agent import PlannerAgent
from app.agents.executor_agent import ExecutorAgent
from app.tools.registry import ToolRegistry


class AgentRunner:

    def __init__(self):
        self.planner = PlannerAgent()
        self.tools = ToolRegistry()
        self.executor = ExecutorAgent(self.tools)

    def run(self, task_prompt: str):
        plan = self.planner.create_plan(task_prompt)
        results = self.executor.execute(plan)

        return {
            "plan": plan,
            "results": results
        }
