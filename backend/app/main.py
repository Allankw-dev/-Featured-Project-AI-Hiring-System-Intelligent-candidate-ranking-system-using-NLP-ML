from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
import os

class ChatMessage(BaseModel):
    message: str
    history: list = []

@app.post("/chat")
async def chat(payload: ChatMessage):
    ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
    
    system = """You are Hira, an AI assistant for an AI-powered hiring platform. You help both candidates and admins.

PLATFORM DETAILS:
- Built with FastAPI backend, Streamlit frontend, PostgreSQL on Supabase
- AI scoring: Semantic (45%), Skills (25%), Experience (20%), Verification (10%)
- Features: Resume upload, AI scoring, job matching, fraud detection, admin panel
- Fraud detection: keyword stuffing, inconsistent dates, short resumes, missing contact info
- Candidates: sign up, upload resumes, apply for jobs, track applications in dashboard
- Admins: post/edit/delete jobs, view top candidates, shortlist/reject, send emails

Be helpful, concise, friendly and accurate. Answer ANY question asked.
Keep responses under 200 words unless more detail is needed."""

    messages = payload.history + [{"role": "user", "content": payload.message}]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 1000,
                "system": system,
                "messages": messages
            },
            timeout=30.0
        )
        data = response.json()
        return {"reply": data["content"][0]["text"]}