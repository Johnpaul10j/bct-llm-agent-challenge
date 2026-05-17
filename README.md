## 🎯 Competition Submission

- **Task A & Task B**: Fully Implemented
- **Docker Image**: Available
- **Live Demo**: Streamlit UI + FastAPI
- **Solution Paper**: Included
- **Evaluation**: BERTScore, ROUGE, RMSE implemented

# BCT LLM Agent Challenge 2026 🧠

**Culturally-Aware LLM Agents for Dynamic User Modeling & Personalized Recommendation**

A complete solution for **both Task A and Task B** submitted to the DSN × Bluechip Technologies LLM Agent Challenge.

---

## ✨ Key Features

- **Task A (User Modeling)**: Generates realistic star ratings + natural Nigerian-style reviews
- **Task B (Recommendation)**: Delivers personalized, cross-domain recommendations (Food, Fashion, Nollywood, Tech, etc.)
- Strong **Nigerian contextualization** and behavioural fidelity
- Clean FastAPI backend + Beautiful Streamlit frontend
- Fully containerized with Docker
- Powered by Groq (Llama-3.3-70B)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Groq API Key

### Installation

```bash
git clone https://github.com/Johnpaul10j/bct-llm-agent-challenge.git
cd bct-llm-agent-challenge

# Install dependencies
pip install -r requirements.txt

2. Install dependencies
Bash
pip install -r requirements.txt

3. Add your Groq API Key
Create .env file:
envGROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx

4. Run the Application
Terminal 1 — Start FastAPI backend:
docker build -t bct-agent-api .
docker run -p 8000:8000 --env-file .env bct-agent-api

Terminal 2 — Start Streamlit frontend:
# Terminal 1 - FastAPI
uvicorn app.main:app --reload --port 8000

# Terminal 2 - Streamlit
streamlit run app.py


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
```

# 🧪 Endpoints

POST /generate_review → Task A (Review + Rating)
POST /recommend → Task B (Recommendations)

Interactive demo available at Interactive Swagger UI: http://localhost:8000/docs (FastAPI) and Streamlit UI.

# 📊 Evaluation

Review Quality: BERTScore + ROUGE
Rating Accuracy: RMSE
Behavioural Fidelity & Contextual Relevance: Qualitative + Human-like outputs
Strong emphasis on Nigerian contextualization


# 🏆 Submission

Containerized Application: FastAPI + Streamlit (Docker ready)
Solution Paper: Included (Solution_Paper.docx)
Code Repository: Clean, modular, and well-documented


# Author: Umeh Johnpaul(Team=Hall of Fame)
## Competition: DSN X BCT LLM Agent Challenge 2026
