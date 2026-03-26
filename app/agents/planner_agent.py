from app.services.llm_service import LLMService


class PlannerAgent:

    def __init__(self):
        self.llm = LLMService()

    def create_plan(self, task: str):

        response = self.llm.generate(task)

        return [
            "Analyze task",
            "Generate plan using LLM",
            response
        ]
