from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Agent & Automation Platform"
    app_env: str = "dev"
    debug: bool = True

    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "agentdb"
    postgres_host: str = "db"
    postgres_port: int = 5432

    redis_url: str = "redis://redis:6379/0"

    openai_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
