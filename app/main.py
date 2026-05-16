# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="BCT LLM Agent Challenge - Bluechip Tech")

class ReviewRequest(BaseModel):
    persona: str
    product_name: str
    category: str = "General"
    product_description: str = ""

class RecommendationRequest(BaseModel):
    persona: str
    n_recommendations: int = 5

@app.get("/")
async def root():
    return {"message": "BCT LLM Agent Challenge API is running!"}

@app.post("/generate_review")
async def generate_review(request: ReviewRequest):
    """Task 1: Generate Review + Rating"""
    # For now we use simple logic, we'll improve with LLM later
    from app.agents.user_modeling import generate_review_and_rating
    
    result = generate_review_and_rating(
        persona=request.persona,
        product_name=request.product_name,
        category=request.category,
        product_description=request.product_description
    )
    return result

@app.post("/recommend")
async def recommend(request: RecommendationRequest):
    """Task 2: Generate Personalized Recommendations"""
    from app.agents.recommender import generate_recommendations
    
    result = generate_recommendations(
        persona=request.persona,
        n_recommendations=request.n_recommendations
    )
    return result