from app.agents.planner_agent import PlannerAgent
from app.agents.executor_agent import ExecutorAgent
from app.tools.registry import ToolRegistry
from app.memory.memory_store import MemoryStore


class AgentRunner:

    def __init__(self):
        self.planner = PlannerAgent()
        self.tools = ToolRegistry()
        self.executor = ExecutorAgent(self.tools)
        self.memory = MemoryStore()

    def run(self, task_prompt: str, run_id: int = None, db=None):

        # Step 1: Plan
        plan = self.planner.create_plan(task_prompt)

        if db and run_id:
            from app.services.audit_service import AuditService
            AuditService.log(db, run_id, "PLAN_CREATED", str(plan))

        # Step 2: Execute
        results = self.executor.execute(plan)

        # Step 3: Save to memory
        self.memory.save("last_run", str(results))

        if db and run_id:
            from app.services.audit_service import AuditService
            AuditService.log(db, run_id, "EXECUTION_COMPLETED", str(results))

        return {
            "plan": plan,
            "results": results
        }
