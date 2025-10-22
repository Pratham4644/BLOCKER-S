"""
Configuration Management for CodeSahayak
This file loads all your API keys and settings from .env file
"""
import os
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application settings"""
    
    # Core APIs (REQUIRED)
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    composio_api_key: str = Field(..., env="COMPOSIO_API_KEY")
    
    # OpenAI settings
    openai_api_base: str = Field("https://api.openai.com/v1", env="OPENAI_API_BASE")
    
    # Voice APIs (Optional)
    elevenlabs_api_key: str = Field("", env="ELEVENLABS_API_KEY")
    
    # GitHub
    github_token: str = Field("", env="GITHUB_TOKEN")
    
    # Google Workspace (Optional)
    google_client_id: str = Field("", env="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field("", env="GOOGLE_CLIENT_SECRET")
    
    # Notion (Optional)
    notion_api_key: str = Field("", env="NOTION_API_KEY")
    notion_database_id: str = Field("", env="NOTION_DATABASE_ID")
    
    # Communication (Optional)
    slack_bot_token: str = Field("", env="SLACK_BOT_TOKEN")
    telegram_bot_token: str = Field("", env="TELEGRAM_BOT_TOKEN")
    
    # App settings
    environment: str = Field("development", env="ENVIRONMENT")
    debug: bool = Field(True, env="DEBUG")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"  # Ignore extra fields in .env
    
    def print_status(self):
        """Print configuration status"""
        print("=" * 50)
        print("🎯 CodeSahayak Configuration")
        print("=" * 50)
        print(f"✅ OpenAI: {self.openai_api_key[:15]}...")
        print(f"✅ Composio: {self.composio_api_key[:15]}...")
        print(f"✅ GitHub: {'Configured' if self.github_token else 'Not set'}")
        print(f"✅ Notion: {'Configured' if self.notion_api_key else 'Not set'}")
        print(f"✅ ElevenLabs: {'Configured' if self.elevenlabs_api_key else 'Not set'}")
        print(f"⚙️  Environment: {self.environment}")
        print(f"⚙️  API Base: {self.openai_api_base}")
        print("=" * 50)

# Singleton pattern
_settings = None

def get_settings() -> Settings:
    """Get the settings instance"""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings

# Test when run directly
if __name__ == "__main__":
    settings = get_settings()
    settings.print_status()
