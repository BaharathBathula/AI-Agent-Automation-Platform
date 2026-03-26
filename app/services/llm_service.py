import os


class LLMService:

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def generate(self, prompt: str) -> str:

        if not self.api_key:
            return f"[Mock LLM] {prompt}"

        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"[LLM ERROR] {str(e)}"
