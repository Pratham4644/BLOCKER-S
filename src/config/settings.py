"""
Configuration Management for CodeSahayak
"""
import os
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application settings"""
    
    # Core APIs
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    composio_api_key: str = Field(..., env="COMPOSIO_API_KEY")
    github_token: str = Field("", env="GITHUB_TOKEN")
    
    # App settings
    environment: str = Field("development", env="ENVIRONMENT")
    debug: bool = Field(True, env="DEBUG")
    
    class Config:
        env_file = ".env"
        case_sensitive = False
    
    def print_status(self):
        """Print configuration status"""
        print("=" * 50)
        print("🎯 CodeSahayak Configuration")
        print("=" * 50)
        print(f"✅ OpenAI: {self.openai_api_key[:15]}...")
        print(f"✅ Composio: {self.composio_api_key[:15]}...")
        print(f"✅ GitHub: {'Configured' if self.github_token else 'Not set'}")
        print(f"⚙️  Environment: {self.environment}")
        print("=" * 50)

# Singleton instance
_settings = None

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings

if __name__ == "__main__":
    settings = get_settings()
    settings.print_status()