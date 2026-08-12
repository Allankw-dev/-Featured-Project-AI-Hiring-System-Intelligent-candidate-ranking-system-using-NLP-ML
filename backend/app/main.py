import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.core.config import settings
from app.routers import auth, jobs, resumes, applications, admin
from app.routers import users
from app.routers import password_reset
from pydantic import BaseModel
import httpx

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

# ── RATE LIMITER ──
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="AI Hiring Platform", version="1.0.0")

# ── RATE LIMITER SETUP ──
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ── CORS MIDDLEWARE ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── ROUTERS ──
app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(resumes.router)
app.include_router(applications.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(password_reset.router)


@app.api_route("/", methods=["GET", "HEAD"])
def home():
    return {"message": "AI Hiring Platform API is running"}


@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return {"status": "ok"}


class ChatMessage(BaseModel):
    message: str
    history: list = []


@app.post("/chat")
async def chat(payload: ChatMessage):
    ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

    if not ANTHROPIC_API_KEY:
        return {"reply": "Chat is temporarily unavailable — missing API key configuration."}

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

    try:
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

            if response.status_code != 200:
                error_msg = data.get('error', {}).get('message', 'unknown error')
                print(f"Claude API error: {error_msg}")
                return {"reply": "Sorry, I'm having trouble right now. Please try again!"}

            return {"reply": data["content"][0]["text"]}

    except httpx.TimeoutException:
        return {"reply": "Request timed out. Please try again!"}
    except Exception as e:
        print(f"Chat error: {str(e)}")
        return {"reply": "Sorry, something went wrong. Please try again!"}