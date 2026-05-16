from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

print("API Key loaded:", "Yes" if os.getenv("GROQ_API_KEY") else "No")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",   # ← Updated model
    temperature=0.7,
    max_tokens=800,
    api_key=os.getenv("GROQ_API_KEY")
)

response = llm.invoke([HumanMessage(content="Hello, say something in Nigerian Pidgin English")])
print("Groq Response:", response.content)