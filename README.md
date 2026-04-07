# 🚀 AI Customer Support Triage Environment

## 📌 Overview
This project simulates a real-world customer support system where an AI agent must:
- Classify support tickets
- Assign priority levels
- Decide appropriate actions
- Generate professional responses

## 🧠 Key Features
- Multi-step decision making
- Realistic customer scenarios
- Semantic reward grading (0–1)
- LLM-powered agent (Groq - LLaMA3)

## ⚙️ Tech Stack
- FastAPI
- Pydantic
- Docker
- Groq LLM

## 🧪 Evaluation
The agent is evaluated on:
- Classification accuracy
- Decision correctness
- Response quality & politeness

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload