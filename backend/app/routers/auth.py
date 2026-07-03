from datetime import datetime
import os

from fastapi import APIRouter, Depends, HTTPException, Request, status
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlalchemy.orm import Session

from app.core.dep import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User
from app.schemas.auth import SignupRequest, LoginRequest, TokenResponse, AdminOTPVerifyRequest
from app.schemas.user import UserOut
from app.services.otp_service import generate_otp, otp_expiration

router = APIRouter(prefix="/auth", tags=["Authentication"])
limiter = Limiter(key_func=get_remote_address)

ADMIN_EMAILS = [e.strip() for e in os.environ.get("ADMIN_EMAILS", "allankamauw20@gmail.com").split(",")]


@router.post("/signup", response_model=UserOut)
@limiter.limit("3/minute")
def signup(request: Request, payload: SignupRequest, db: Session = Depends(get_db)):
    try:
        existing = db.query(User).filter(User.email == payload.email).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        role = "admin" if payload.email in ADMIN_EMAILS else "candidate"

        user = User(
            full_name=payload.full_name,
            email=payload.email,
            password_hash=hash_password(payload.password),
            role=role,
            is_active=True
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
def login(request: Request, payload: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == payload.email).first()

        # Same error for both wrong email and wrong password (prevents enumeration)
        if not user or not verify_password(payload.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        token = create_access_token({
            "user_id": user.id,
            "email": user.email,
            "role": user.role
        })

        return {
            "access_token": token,
            "token_type": "bearer",
            "role": user.role
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/admin/request-otp")
@limiter.limit("3/minute")
def admin_request_otp(request: Request, payload: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == payload.email).first()

        if not user or not verify_password(payload.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        if user.role != "admin":
            raise HTTPException(status_code=403, detail="Admin access required")

        otp = generate_otp()
        expiry = otp_expiration()

        user.otp_code = otp
        user.otp_expiry = expiry
        db.commit()

        print(f"\nADMIN OTP for {user.email}: {otp}\n")

        return {"message": "OTP generated. Check backend terminal."}

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/admin/verify-otp", response_model=TokenResponse)
@limiter.limit("5/minute")
def admin_verify_otp(request: Request, payload: AdminOTPVerifyRequest, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == payload.email).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if user.role != "admin":
            raise HTTPException(status_code=403, detail="Admin access required")

        if not user.otp_code or not user.otp_expiry:
            raise HTTPException(status_code=400, detail="No OTP requested")

        if user.otp_code != payload.otp_code:
            raise HTTPException(status_code=400, detail="Invalid OTP")

        expiry = user.otp_expiry
        if expiry.tzinfo is None:
            from datetime import timezone
            expiry = expiry.replace(tzinfo=timezone.utc)

        if datetime.now(datetime.timezone.utc) > expiry:
            raise HTTPException(status_code=400, detail="OTP expired")

        user.otp_code = None
        user.otp_expiry = None
        db.commit()

        token = create_access_token({
            "user_id": user.id,
            "email": user.email,
            "role": user.role
        })

        return {
            "access_token": token,
            "token_type": "bearer",
            "role": user.role
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))