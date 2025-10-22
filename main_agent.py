"""
CodeSahayak - Complete Agent (Working Version)
Hackathon Submission - No External Tools Dependency
"""

import asyncio
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferMemory
from src.config.settings import get_settings

class CodeSahayakAgent:
    """Main CodeSahayak Agent - Working Version"""
    
    def __init__(self):
        """Initialize the agent with all components"""
        print("🚀 Initializing CodeSahayak Agent...")
        print("=" * 70)
        
        settings = get_settings()
        
        # Initialize AI (the brain)
        print("🧠 Setting up AI Brain (GPT-3.5)...")
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key="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",
            base_url="https://openrouter.ai/api/v1",
            temperature=0.7
        )
        print("   ✅ AI Brain initialized")
        
        # Agent personality
        self.system_prompt = """You are CodeSahayak, an AI coding mentor for Indian students.

Your Mission:
Help students learn DSA and programming in a friendly, supportive way.

Your Personality:
- Speak in Marathi-English mix (Hinglish style)
- Be encouraging and motivating  
- Use "bro" or "dost" casually
- Add emojis to make it fun
- Explain complex concepts simply

Your Capabilities:
- Review code and find bugs
- Explain DSA concepts clearly
- Give interview preparation tips
- Help with programming assignments
- Suggest learning resources

When helping students:
1. Understand their current level
2. Give clear, simple explanations  
3. Use examples they can relate to
4. Be patient and encouraging
5. Motivate them to keep learning

IMPORTANT: You are a coding mentor. Focus on:
- Code explanations and reviews
- DSA concept explanations  
- Interview preparation guidance
- Debugging help
- Learning path suggestions
"""
        
        # Memory for conversation
        print("\n💾 Setting up Memory...")
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            max_token_limit=2000
        )
        print("   ✅ Memory initialized")
        
        print("\n" + "=" * 70)
        print("✨ CodeSahayak Agent Ready!")
        print("=" * 70 + "\n")
    
    async def chat(self, message: str):
        """Main chat interface"""
        try:
            # Get chat history from memory
            memory_variables = self.memory.load_memory_variables({})
            chat_history = memory_variables.get("chat_history", [])
            
            # Build messages list
            messages = [SystemMessage(content=self.system_prompt)]
            
            # Add conversation history
            for msg in chat_history:
                messages.append(msg)
            
            # Add current message
            messages.append(HumanMessage(content=message))
            
            print(f"💬 Processing: {message[:50]}...")
            
            # Get response from LLM
            response = await self.llm.ainvoke(messages)
            
            # Save to memory
            self.memory.save_context(
                {"input": message},
                {"output": response.content}
            )
            
            return response.content
            
        except Exception as e:
            error_msg = f"Sorry bro, technical error आली 😅\nError: {str(e)[:100]}"
            print(f"❌ Error in chat: {e}")
            return error_msg


async def demo():
    """Demo function to test the agent"""
    print("\n" + "=" * 70)
    print("🎯 CodeSahayak - Complete Agent Demo")
    print("=" * 70 + "\n")
    
    # Create agent
    agent = CodeSahayakAgent()
    
    # Test scenarios
    scenarios = [
        "मला bubble sort समजावून सांग",
        "Can you help me review my code? I have a function that should find the maximum number in a list but it's not working",
        "Interview preparation tips दे for fresher",
        "What is recursion and how does it work?",
        "Python मध्ये list comprehension कसे use करतात?",
        "माझ्याकडे array चा problem आहे, मदत करशील का?"
    ]
    
    for i, message in enumerate(scenarios, 1):
        print(f"\n📝 Scenario {i}/{len(scenarios)}")
        print("-" * 70)
        print(f"💬 Student: {message}")
        print("-" * 70)
        
        response = await agent.chat(message)
        
        print(f"\n🤖 CodeSahayak:\n{response}")
        print("\n" + "=" * 70)
        
        # Small delay to make it feel natural
        await asyncio.sleep(1)
    
    print("\n✨ Demo Complete! 🚀")
    print("CodeSahayak is ready to help students! 📚\n")


async def interactive_chat():
    """Interactive chat mode"""
    print("\n" + "=" * 70)
    print("💬 CodeSahayak - Interactive Mode")
    print("Type 'exit' or 'quit' to end the conversation")
    print("=" * 70 + "\n")
    
    agent = CodeSahayakAgent()
    
    while True:
        try:
            user_input = input("\n🎯 You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 CodeSahayak: Bye dost! Happy coding! 🚀")
                break
            
            if not user_input:
                continue
                
            print("🤖 CodeSahayak: Thinking...")
            response = await agent.chat(user_input)
            print(f"\n🤖 CodeSahayak: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 CodeSahayak: Aapla swagat ahe! Come back soon! 🙏")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            continue


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        asyncio.run(interactive_chat())
    else:
        print("\n🎬 Running CodeSahayak Demo...\n")
        asyncio.run(demo())