# app/agents/recommender.py
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.core.prompts import RECOMMENDATION_PROMPT
import json
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=800,
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_recommendations(persona: str, n_recommendations: int = 5):
    prompt = RECOMMENDATION_PROMPT.format(persona=persona, n=n_recommendations)
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        text = response.content.strip()
        
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].strip()
        
        recs = json.loads(text)
        return {"recommendations": recs}
        
    except Exception as e:
        print("Error in recommendation:", e)
        return {"recommendations": []}