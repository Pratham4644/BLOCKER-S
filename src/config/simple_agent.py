"""
Simple CodeSahayak Agent - MVP Version
"""
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

class SimpleCodeMentor:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.7
        )
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are CodeSahayak, a friendly AI coding mentor.
            
            You help Indian students with programming and DSA.
            Speak in a mix of Marathi and English (Hinglish style).
            Be encouraging and supportive.
            Call the student "bro" or "dost" casually."""),
            ("human", "{question}")
        ])
        
        self.chain = self.prompt | self.llm
    
    async def ask(self, question: str) -> str:
        """Ask the mentor a question"""
        response = await self.chain.ainvoke({"question": question})
        return response.content

# Test it
async def test_mentor():
    mentor = SimpleCodeMentor()
    
    questions = [
        "What is bubble sort?",
        "मला recursion समजत नाही, help कर",
        "How to prepare for coding interviews?"
    ]
    
    for q in questions:
        print(f"\n🎤 Student: {q}")
        answer = await mentor.ask(q)
        print(f"🤖 CodeSahayak: {answer}\n")
        print("-" * 50)

if __name__ == "__main__":
    import asyncio
    print("🎓 Testing Simple CodeSahayak Agent...\n")
    asyncio.run(test_mentor())