"""
CodeSahayak - ULTIMATE Working Solution
Combines Composio + Direct SMTP fallback
"""

import sys
sys.path.insert(0, '.')

import os
from src.config.settings import get_settings
from composio import ComposioToolSet, Action
from langchain_openai import ChatOpenAI
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class CodeSahayakUltimate:
    """Ultimate CodeSahayak with multiple fallbacks"""
    
    def __init__(self):
        self.settings = get_settings()
        self.toolset = ComposioToolSet(api_key=self.settings.composio_api_key)
        self.llm = ChatOpenAI(
            model="openai/gpt-4o-mini",
            openai_api_key=self.settings.openai_api_key,
            openai_api_base=self.settings.openai_api_base,
            temperature=0.7
        )
        print("✅ CodeSahayak Ultimate initialized")
    
    # ============ GITHUB (With Fallback to Direct API) ============
    
    def github_get_file(self, owner: str, repo: str, path: str):
        """Get file from GitHub - tries Composio, falls back to direct API"""
        
        # Method 1: Try Composio
        try:
            print("   🔄 Trying Composio for GitHub...")
            result = self.toolset.execute_action(
                action=Action.GITHUB_GET_THE_CONTENTS_OF_A_FILE_IN_A_REPOSITORY,
                params={
                    "owner": owner,
                    "repo": repo,
                    "path": path
                }
            )
            print("   ✅ GitHub via Composio worked!")
            return {"success": True, "method": "composio", "data": result}
        except Exception as e:
            print(f"   ⚠️  Composio failed: {str(e)[:80]}")
        
        # Method 2: Fallback to GitHub API directly
        try:
            print("   🔄 Trying direct GitHub API...")
            import requests
            import base64
            
            url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
            headers = {
                "Accept": "application/vnd.github.v3+json"
            }
            
            # Add token if available
            github_token = os.getenv("GITHUB_TOKEN")
            if github_token:
                headers["Authorization"] = f"token {github_token}"
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            content = base64.b64decode(data['content']).decode('utf-8')
            
            print("   ✅ GitHub via Direct API worked!")
            return {
                "success": True,
                "method": "direct_api",
                "data": {"content": content, "path": path}
            }
        except Exception as e:
            print(f"   ❌ Direct API also failed: {e}")
            return {"success": False, "error": str(e)}
    
    # ============ CODE ANALYSIS ============
    
    def analyze_code(self, code: str, language: str = "python"):
        """Analyze code - this ALWAYS works!"""
        prompt = f"""तू एक coding mentor आहेस. Analyze this {language} code:

```{language}
{code}
```

Provide in Marathi-English mix:
1. Code Quality (1-10)
2. Bugs (if any)
3. Time Complexity
4. Suggestions

Keep it short and practical."""

        try:
            response = self.llm.invoke(prompt)
            return {"success": True, "analysis": response.content}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    # ============ EMAIL (Multiple Methods) ============
    
    def send_email(self, to: str, subject: str, body: str):
        """Send email - tries Composio, then SMTP, then mock"""
        
        # Method 1: Try Composio
        try:
            print("   🔄 Trying Composio for Gmail...")
            result = self.toolset.execute_action(
                action=Action.GMAIL_SEND_AN_EMAIL,
                params={
                    "to": to,
                    "subject": subject,
                    "body": body
                }
            )
            print("   ✅ Email sent via Composio!")
            return {"success": True, "method": "composio", "data": result}
        except Exception as e:
            print(f"   ⚠️  Composio failed: {str(e)[:80]}")
        
        # Method 2: Try SMTP
        smtp_email = os.getenv("GMAIL_SMTP_EMAIL")
        smtp_password = os.getenv("GMAIL_APP_PASSWORD")
        
        if smtp_email and smtp_password:
            try:
                print("   🔄 Trying SMTP...")
                
                msg = MIMEMultipart('alternative')
                msg['From'] = smtp_email
                msg['To'] = to
                msg['Subject'] = subject
                
                # HTML version
                html = f"""
                <html>
                <body style="font-family: Arial; padding: 20px;">
                    <h2 style="color: #4285f4;">🚀 CodeSahayak Analysis</h2>
                    <div style="background: #f5f5f5; padding: 15px; border-radius: 5px;">
                        <pre style="white-space: pre-wrap;">{body}</pre>
                    </div>
                    <p style="color: #666; font-size: 12px;">
                        CodeSahayak - Your AI Coding Mentor 🤖
                    </p>
                </body>
                </html>
                """
                
                part1 = MIMEText(body, 'plain')
                part2 = MIMEText(html, 'html')
                msg.attach(part1)
                msg.attach(part2)
                
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login(smtp_email, smtp_password)
                    server.send_message(msg)
                
                print(f"   ✅ Email sent via SMTP to {to}!")
                return {"success": True, "method": "smtp"}
                
            except Exception as e:
                print(f"   ⚠️  SMTP failed: {e}")
        else:
            print("   ⚠️  SMTP credentials not configured")
        
        # Method 3: Mock for demo
        print("   🎬 Using MOCK mode for demo")
        print(f"   📧 Would send to: {to}")
        print(f"   📝 Subject: {subject}")
        print(f"   💬 Body: {body[:100]}...")
        return {
            "success": True,
            "method": "mock",
            "note": "Demo mode - check console output"
        }
    
    # ============ NOTION (With Mock Fallback) ============
    
    def notion_create_page(self, database_id: str, title: str, content: str):
        """Create Notion page"""
        try:
            print("   🔄 Trying Composio for Notion...")
            result = self.toolset.execute_action(
                action=Action.NOTION_CREATE_A_PAGE,
                params={
                    "parent": {"database_id": database_id},
                    "properties": {
                        "title": [{"text": {"content": title}}]
                    }
                }
            )
            print("   ✅ Notion page created!")
            return {"success": True, "method": "composio", "data": result}
        except Exception as e:
            print(f"   ⚠️  Notion: {str(e)[:80]}")
            print("   🎬 Using MOCK mode")
            return {
                "success": True,
                "method": "mock",
                "note": f"Would create page: {title}"
            }
    
    # ============ COMPLETE WORKFLOW ============
    
    def run_demo_workflow(self, user_email: str = "prathamps8666@gmail.com"):
        """
        Complete demo workflow with sample code
        Perfect for your demo video!
        """
        
        print("\n" + "="*70)
        print("🚀 CodeSahayak - Complete Demo Workflow")
        print("="*70)
        
        # Sample code to analyze
        sample_code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test
numbers = [64, 34, 25, 12, 22, 11, 90]
result = bubble_sort(numbers)
print(result)
"""
        
        results = {}
        
        # Step 1: Analyze code
        print("\n1️⃣ Analyzing code...")
        analysis_result = self.analyze_code(sample_code)
        
        if not analysis_result['success']:
            print(f"❌ Analysis failed: {analysis_result['error']}")
            return {"success": False, "step": "analysis"}
        
        analysis = analysis_result['analysis']
        print(f"✅ Analysis complete!")
        print(f"\nAnalysis Preview:\n{analysis[:200]}...\n")
        results['analysis'] = analysis_result
        
        # Step 2: Send email
        print("2️⃣ Sending email notification...")
        email_result = self.send_email(
            to=user_email,
            subject="✅ Code Analysis Complete - bubble_sort.py",
            body=f"""नमस्कार Prathamesh! 👋

तुझा code analysis complete झाला आहे!

📁 File: bubble_sort.py

📊 Analysis:
{analysis}

---
Keep coding! 💻
CodeSahayak"""
        )
        
        print(f"✅ Email: {email_result['method']} method used")
        results['email'] = email_result
        
        # Step 3: Notion
        print("\n3️⃣ Saving to Notion...")
        notion_result = self.notion_create_page(
            database_id="demo-db-id",
            title="Code Analysis - bubble_sort.py",
            content=analysis[:500]
        )
        print(f"✅ Notion: {notion_result['method']} method used")
        results['notion'] = notion_result
        
        # Summary
        print("\n" + "="*70)
        print("✨ WORKFLOW COMPLETE!")
        print("="*70)
        
        print("\n📊 Results Summary:")
        print(f"   ✅ Code Analysis: Success")
        print(f"   ✅ Email: {results['email']['method']}")
        print(f"   ✅ Notion: {results['notion']['method']}")
        
        if results['email']['method'] == 'smtp':
            print(f"\n📧 CHECK YOUR EMAIL: {user_email}")
            print("   Real email was sent!")
        elif results['email']['method'] == 'mock':
            print("\n🎬 Demo Mode Active")
            print("   Setup SMTP for real emails (see guide below)")
        
        return {"success": True, "results": results}
    
    def run_github_workflow(self, owner: str, repo: str, file_path: str, 
                           user_email: str = "prathamps8666@gmail.com"):
        """Workflow with real GitHub file"""
        
        print("\n" + "="*70)
        print("🚀 CodeSahayak - GitHub Workflow")
        print("="*70)
        
        # Step 1: Get file from GitHub
        print(f"\n1️⃣ Fetching {file_path} from GitHub...")
        github_result = self.github_get_file(owner, repo, file_path)
        
        if not github_result['success']:
            print(f"❌ GitHub failed: {github_result['error']}")
            return {"success": False, "step": "github"}
        
        # Extract code
        if github_result['method'] == 'composio':
            code = github_result['data'].get('data', {}).get('content', '')
        else:
            code = github_result['data'].get('content', '')
        
        print(f"✅ Code fetched via {github_result['method']}!")
        print(f"   {len(code)} characters")
        
        # Step 2: Analyze
        print("\n2️⃣ Analyzing code...")
        analysis_result = self.analyze_code(code[:1000])  # Limit for demo
        
        if not analysis_result['success']:
            print(f"❌ Analysis failed")
            return {"success": False, "step": "analysis"}
        
        analysis = analysis_result['analysis']
        print(f"✅ Analysis done!")
        
        # Step 3: Send email
        print("\n3️⃣ Sending email...")
        email_result = self.send_email(
            to=user_email,
            subject=f"Code Analysis: {file_path}",
            body=f"Analysis:\n\n{analysis}"
        )
        print(f"✅ Email: {email_result['method']}")
        
        print("\n" + "="*70)
        print("✨ COMPLETE!")
        print("="*70)
        
        return {"success": True}


# ============ SMTP SETUP GUIDE ============

def show_smtp_setup():
    print("\n" + "="*70)
    print("📧 Quick SMTP Setup (5 minutes)")
    print("="*70)
    print("""
1. Go to: https://myaccount.google.com/apppasswords
2. Generate App Password for "Mail"
3. Add to .env:

GMAIL_SMTP_EMAIL=prathamps8666@gmail.com
GMAIL_APP_PASSWORD=your-16-char-password

4. Run again - real emails will be sent!
    """)
    print("="*70)


# ============ MAIN ============

if __name__ == "__main__":
    print("="*70)
    print("🎯 CodeSahayak Ultimate - Demo Ready!")
    print("="*70)
    
    sahayak = CodeSahayakUltimate()
    
    # Check SMTP setup
    smtp_configured = os.getenv("GMAIL_SMTP_EMAIL") and os.getenv("GMAIL_APP_PASSWORD")
    
    if smtp_configured:
        print("\n✅ SMTP Configured - Will send REAL emails!")
    else:
        print("\n⚠️  SMTP Not Configured - Will use MOCK mode")
        print("   (Perfect for demo video, or setup SMTP for real emails)")
    
    # Run demo workflow
    print("\n" + "="*70)
    print("Running Demo Workflow...")
    print("="*70)
    
    result = sahayak.run_demo_workflow(user_email="prathamps8666@gmail.com")
    
    if not smtp_configured:
        show_smtp_setup()
    
    print("\n💡 Other workflows:")
    print("\n# For GitHub workflow:")
    print("sahayak.run_github_workflow('python', 'cpython', 'README.rst')")
    
    print("\n🎬 Ready for demo video!")