import os
from dotenv import load_dotenv

load_dotenv()

print("🔍 Checking setup...\n")

# Check Python packages
try:
    import langchain
    import composio
    import openai
    print("✅ Core packages installed")
except ImportError as e:
    print(f"❌ Missing package: {e}")

# Check API keys
required_keys = ["OPENAI_API_KEY", "COMPOSIO_API_KEY"]
for key in required_keys:
    if os.getenv(key):
        print(f"✅ {key} found")
    else:
        print(f"❌ {key} missing!")

print("\n✨ Setup check complete!")