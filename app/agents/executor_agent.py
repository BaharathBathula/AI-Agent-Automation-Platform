class ExecutorAgent:

    def __init__(self, tools_registry):
        self.tools_registry = tools_registry

        # Register default tools
        from app.tools.web_search_tool import WebSearchTool
        self.tools_registry.register("web_search", WebSearchTool())

    def execute(self, steps: list):

        results = []

        for step in steps:

            if "search" in step.lower():
                tool = self.tools_registry.get("web_search")
                output = tool.run(step)
                results.append(output)

            else:
                results.append(f"Executed: {step}")

        return results
