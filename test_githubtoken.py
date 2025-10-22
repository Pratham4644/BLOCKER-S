import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"token {token}"}

# Test API access
response = requests.get("https://api.github.com/user", headers=headers)

if response.status_code == 200:
    user = response.json()
    print(f"✅ GitHub token works!")
    print(f"👤 Logged in as: {user['login']}")
    print(f"📧 Email: {user.get('email', 'Not public')}")
else:
    print(f"❌ Token error: {response.status_code}")
    Narration: "How does it work?