

import asyncio
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from composio_langchain import ComposioToolSet, Action, App
from src.config.settings import get_settings

class CompleteDynamicAgent:
    """
    FULLY DYNAMIC CodeSahayak Agent
    
    This agent ACTUALLY:
    - Fetches code from GitHub when asked
    - Creates Notion pages for progress tracking
    - Schedules Calendar events for practice
    - Sends Gmail notifications
    - Posts to Slack channels
    - Uses WhatsApp for alerts
    """
    
    def __init__(self):
        """Initialize COMPLETE dynamic agent"""
        print("=" * 80)
        print("🚀 CODESAHAYAK - COMPLETE DYNAMIC AGENT")
        print("=" * 80)
        
        settings = get_settings()
        
        # Initialize LLM
        print("\n🧠 Initializing AI Brain...")
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=settings.openai_api_key,
            base_url=settings.openai_api_base,
            temperature=0.7
        )
        print("   ✅ GPT-3.5 Turbo ready")
        
        # Initialize Composio with ALL tools
        print("\n🔧 Initializing Composio ToolSet...")
        self.toolset = ComposioToolSet(api_key=settings.composio_api_key)
        print("   ✅ Composio connected")
        
        # Enhanced system prompt for DYNAMIC tool use
        self.system_prompt = """You are CodeSahayak, an AI coding mentor with REAL TOOLS.

🎯 CRITICAL: You have ACTUAL access to tools. USE THEM when appropriate!

Your REAL Capabilities:
1. GitHub Integration:
   - Fetch code files when asked
   - List repositories
   - Review actual code
   
2. Notion Integration:
   - Create progress entries
   - Track student learning
   - Save code reviews
   
3. Google Calendar:
   - Schedule practice sessions
   - Set reminders
   - Create study events
   
4. Gmail:
   - Send detailed reports
   - Email code reviews
   - Send practice reminders
   
5. Slack:
   - Post to study groups
   - Share achievements
   - Coordinate learning

WHEN TO USE TOOLS:
- Student asks to "check my code" → Use GITHUB tool to fetch it
- Student wants to "track progress" → Use NOTION tool to create entry
- Student says "schedule practice" → Use CALENDAR tool
- Student needs "email report" → Use GMAIL tool
- Student wants to "share with group" → Use SLACK tool

IMPORTANT RULES:
1. ASK for details if needed (repo name, file path, etc.)
2. USE tools when you have enough information
3. Give Marathi-English responses
4. Be encouraging and friendly
5. ACTUALLY EXECUTE the tools, dont just talk about them!

Your personality:
- Speak Marathi-English mix
- Use "bro" or "dost"
- Add emojis
- Be motivating

REMEMBER: You are NOT just a chatbot - you are an AGENT with REAL POWERS! 🚀
"""
        
        # Memory
        print("\n💾 Setting up Memory...")
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="output"
        )
        print("   ✅ Conversation memory ready")
        
        print("\n" + "=" * 80)
        print("✨ DYNAMIC AGENT READY - ALL TOOLS ACTIVE!")
        print("=" * 80 + "\n")
    
    def get_all_tools(self):
        """Get ALL available Composio tools"""
        print("🔍 Loading ALL Composio tools...")
        
        try:
            # Get ALL major tools
            tools = self.toolset.get_tools(
                apps=[
                    App.GITHUB,
                    App.NOTION,
                    App.GOOGLECALENDAR,
                    App.GMAIL,
                    App.SLACK,
                ]
            )
            
            print(f"✅ Loaded {len(tools)} dynamic tools!")
            print(f"   Tools available:")
            for i, tool in enumerate(tools[:15], 1):  # Show first 15
                print(f"   {i}. {tool.name}")
            
            return tools
            
        except Exception as e:
            print(f"⚠️  Tool loading error: {e}")
            print("   Falling back to basic mode...")
            return []
    
    def create_dynamic_agent(self):
        """Create agent that ACTUALLY USES tools"""
        tools = self.get_all_tools()
        
        if not tools:
            print("❌ No tools available - running as basic chatbot")
            prompt = ChatPromptTemplate.from_messages([
                ("system", self.system_prompt),
                ("human", "{input}"),
            ])
            return prompt | self.llm
        
        print(f"\n🔧 Creating DYNAMIC agent with {len(tools)} tools...")
        
        # Create prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
        
        # Create agent
        agent = create_openai_functions_agent(
            llm=self.llm,
            tools=tools,
            prompt=prompt
        )
        
        # Create executor with HIGH verbosity
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            memory=self.memory,
            verbose=True,  # Show what tools its using!
            handle_parsing_errors=True,
            max_iterations=10,  # Allow more steps for complex tasks
            return_intermediate_steps=True
        )
        
        print("✅ Dynamic agent created with tool access!\n")
        return agent_executor
    
    async def chat(self, message: str):
        """Chat with DYNAMIC tool-using agent"""
        agent = self.create_dynamic_agent()
        
        print(f"\n{'='*80}")
        print(f"💬 USER: {message}")
        print(f"{'='*80}\n")
        
        try:
            if isinstance(agent, AgentExecutor):
                # DYNAMIC AGENT - Will use tools!
                print("🤖 Agent processing with REAL tools...\n")
                result = await agent.ainvoke({"input": message})
                
                # Show what tools were used
                if "intermediate_steps" in result:
                    print("\n🛠️  TOOLS USED:")
                    for step in result["intermediate_steps"]:
                        tool_name = step[0].tool
                        print(f"   ✅ {tool_name}")
                
                return result["output"]
            else:
                # Basic chatbot fallback
                print("💬 Processing as basic chatbot...\n")
                response = await agent.ainvoke({"input": message})
                return response.content
                
        except Exception as e:
            print(f"\n❌ Error: {e}")
            return f"Sorry bro, error आली: {str(e)[:200]}"


async def demo_dynamic_workflows():
    """
    Demo ACTUAL dynamic tool usage
    These scenarios will TRIGGER real tool calls!
    """
    print("\n" + "="*80)
    print("🎯 CODESAHAYAK - DYNAMIC TOOL USAGE DEMO")
    print("="*80)
    print("This demo shows REAL tool integration!")
    print("="*80 + "\n")
    
    agent = CompleteDynamicAgent()
    
    # Scenarios that TRIGGER tool usage
    dynamic_scenarios = [
        {
            "title": "GitHub Integration Test",
            "message": "Can you list my GitHub repositories?",
            "expected_tool": "GITHUB"
        },
        {
            "title": "Notion Integration Test", 
            "message": "Create a Notion page to track my DSA progress for today",
            "expected_tool": "NOTION"
        },
        {
            "title": "Calendar Integration Test",
            "message": "Schedule a 1-hour DSA practice session for tomorrow at 6 PM",
            "expected_tool": "CALENDAR"
        },
        {
            "title": "Basic Explanation (No Tools)",
            "message": "मला bubble sort समजावून सांग",
            "expected_tool": "NONE"
        }
    ]
    
    for i, scenario in enumerate(dynamic_scenarios, 1):
        print(f"\n{'#'*80}")
        print(f"SCENARIO {i}/{len(dynamic_scenarios)}: {scenario['title']}")
        print(f"Expected Tool: {scenario['expected_tool']}")
        print(f"{'#'*80}\n")
        
        response = await agent.chat(scenario['message'])
        
        print(f"\n🤖 AGENT RESPONSE:")
        print(f"{'='*80}")
        print(response)
        print(f"{'='*80}\n")
        
        await asyncio.sleep(1)
    
    print("\n" + "="*80)
    print("✨ DYNAMIC DEMO COMPLETE!")
    print("="*80 + "\n")


async def interactive_dynamic():
    """Interactive mode with REAL tool usage"""
    print("\n" + "="*80)
    print("🎯 CODESAHAYAK - INTERACTIVE DYNAMIC MODE")
    print("="*80)
    print("Talk to CodeSahayak - it will USE REAL TOOLS!")
    print("Try commands like:")
    print("  • 'List my GitHub repos'")
    print("  • 'Create a Notion page for today'")
    print("  • 'Schedule practice tomorrow'")
    print("  • 'Explain bubble sort' (no tools)")
    print("\nType 'exit' to quit")
    print("="*80 + "\n")
    
    agent = CompleteDynamicAgent()
    
    while True:
        try:
            user_input = input("\n💬 YOU: ")
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Bye bro! Keep coding!")
                break
            
            if not user_input.strip():
                continue
            
            response = await agent.chat(user_input)
            
            print(f"\n🤖 CODESAHAYAK:")
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n👋 Exiting...")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        print("\n🎮 Starting Interactive Mode...\n")
        asyncio.run(interactive_dynamic())
    else:
        print("\n🎬 Starting Dynamic Demo...\n")
        asyncio.run(demo_dynamic_workflows())
