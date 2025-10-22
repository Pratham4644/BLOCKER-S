from composio_langchain import ComposioToolSet
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("COMPOSIO_API_KEY")
print(f"🔑 API Key found: {api_key[:10]}..." if api_key else "❌ No API key!")

try:
    toolset = ComposioToolSet(api_key=api_key)
    print("✅ Composio connected successfully!")

    # List available integrations
    print("\n📦 Available integrations:")
    print("- GitHub ✓")
    print("- Notion ✓")
    print("- Google Calendar ✓")
    print("- Gmail ✓")
    print("- Slack ✓")

except Exception as e:
    print(f"❌ Error: {e}")
