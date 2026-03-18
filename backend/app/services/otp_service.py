import secrets
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.models.user import User


# ------------------------------
# GENERATE OTP
# ------------------------------
def generate_otp() -> str:
    """
    Generate a secure 6-digit OTP
    """
    return f"{secrets.randbelow(900000) + 100000}"


# ------------------------------
# OTP EXPIRATION
# ------------------------------
def otp_expiration(minutes: int = 5) -> datetime:
    """
    Set OTP expiration time (default: 5 minutes)
    """
    return datetime.utcnow() + timedelta(minutes=minutes)


# ------------------------------
# SAVE OTP TO USER
# ------------------------------
def save_otp(db: Session, user: User) -> str:
    """
    Generate and store OTP in DB
    """
    otp = generate_otp()
    expiry = otp_expiration()

    user.otp_code = otp
    user.otp_expiry = expiry

    db.commit()

    return otp


# ------------------------------
# VERIFY OTP
# ------------------------------
def verify_otp(db: Session, user: User, otp_code: str) -> bool:
    """
    Verify OTP validity
    """
    if not user.otp_code or not user.otp_expiry:
        return False

    if user.otp_code != otp_code:
        return False

    if datetime.utcnow() > user.otp_expiry:
        return False

    return True


# ------------------------------
# CLEAR OTP AFTER USE
# ------------------------------
def clear_otp(db: Session, user: User):
    """
    Remove OTP after successful verification
    """
    user.otp_code = None
    user.otp_expiry = None
    db.commit()