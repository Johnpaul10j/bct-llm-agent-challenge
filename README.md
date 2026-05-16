## 🎯 Competition Submission

- **Task A & Task B**: Fully Implemented
- **Docker Image**: Available
- **Live Demo**: Streamlit UI + FastAPI
- **Solution Paper**: Included
- **Evaluation**: BERTScore, ROUGE, RMSE implemented

# BCT LLM Agent Challenge 2026

**Culturally-Aware LLM Agents for User Modeling and Personalized Recommendation**

A complete solution for **Task A (User Modeling)** and **Task B (Recommendation)** submitted to the DSN × Bluechip Technologies LLM Agent Challenge.

---

## ✨ Features

- **Task A**: Generate realistic star ratings + natural Nigerian-style reviews from user persona
- **Task B**: Deliver personalized, cross-domain recommendations (Food, Fashion, Movies, Tech, etc.)
- Culturally adapted for Nigerian users (balanced English with local flavor)
- Clean FastAPI backend + Beautiful Streamlit frontend
- Powered by Groq (Llama-3.3-70B)

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd bct-llm-agent-challenge

2. Install dependencies
Bashpip install -r requirements.txt

3. Add your Groq API Key
Create .env file:
envGROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx

4. Run the Application
Terminal 1 — Start FastAPI backend:
Bashuvicorn app.main:app --reload --port 8000
Terminal 2 — Start Streamlit frontend:
Bashstreamlit run app.py

📁 Project Structure
textbct-llm-agent-challenge/
├── app/
│   ├── main.py                 # FastAPI endpoints
│   ├── agents/
│   │   ├── user_modeling.py
│   │   └── recommender.py
│   └── core/
│       └── prompts.py
├── app.py                      # Streamlit UI
├── evaluation.py               # BERTScore, RMSE, etc.
├── requirements.txt
├── Dockerfile
├── Solution_Paper.docx
└── README.md

🧪 Endpoints

POST /generate_review → Task A (Review + Rating)
POST /recommend → Task B (Recommendations)

Interactive demo available at /docs (FastAPI) and Streamlit UI.

📊 Evaluation

Review Quality: BERTScore + ROUGE
Rating Accuracy: RMSE
Behavioural Fidelity & Contextual Relevance: Qualitative + Human-like outputs
Strong emphasis on Nigerian contextualization


🏆 Submission

Containerized Application: FastAPI + Streamlit (Docker ready)
Solution Paper: Included (Solution_Paper.docx)
Code Repository: Clean, modular, and well-documented


Author: Umeh Johnpaul
Competition: DSN X BCT LLM Agent Challenge 2026