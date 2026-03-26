from typing import List


class PlannerAgent:
    """
    Responsible for breaking down user tasks into structured steps.
    """

    def __init__(self):
        pass

    def create_plan(self, task: str) -> List[str]:
        """
        Convert user input into step-by-step execution plan.
        """

        # Simple rule-based plan (will upgrade later with LLM)
        steps = [
            "Understand the task",
            "Identify required data sources",
            "Select appropriate tools",
            "Execute step-by-step actions",
            "Aggregate results",
            "Generate final response"
        ]

        return steps
