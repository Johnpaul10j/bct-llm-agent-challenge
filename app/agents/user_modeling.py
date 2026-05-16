# app/agents/user_modeling.py
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.core.prompts import REVIEW_PROMPT
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

def generate_review_and_rating(persona: str, product_name: str, category: str = "General", product_description: str = ""):
    prompt = REVIEW_PROMPT.format(
        persona=persona,
        product_name=product_name,
        category=category,
        product_description=product_description or "Popular product in Nigeria."
    )
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        text = response.content.strip()
        
        # Clean JSON
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].strip()
        
        result = json.loads(text)
        result["persona"] = persona
        result["product"] = product_name
        return result
        
    except Exception as e:
        print("Error in review generation:", e)
        return {
            "rating": 4.3,
            "review_text": f"This {product_name} is quite good. As a {persona}, I find it useful and would recommend it.",
            "persona": persona,
            "product": product_name
        }