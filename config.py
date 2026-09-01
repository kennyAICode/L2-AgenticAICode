import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model: str = os.getenv("AGENT_MODEL", "tinyllama")
    ollama_url: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()

