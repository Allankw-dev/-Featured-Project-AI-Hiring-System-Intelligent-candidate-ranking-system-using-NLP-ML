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
    allow_origins=[
        "https://ai-powered-hiring-system.streamlit.app",
        "http://localhost:8501",
    ],
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