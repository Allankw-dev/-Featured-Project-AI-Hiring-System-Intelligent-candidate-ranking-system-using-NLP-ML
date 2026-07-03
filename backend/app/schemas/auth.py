from pydantic import BaseModel, EmailStr, validator


class SignupRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    sex: str

    @validator("password")
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one number")
        return v

    @validator("full_name")
    def name_valid(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Full name must be at least 2 characters")
        if any(c.isdigit() for c in v):
            raise ValueError("Full name cannot contain numbers")
        return v.strip()

    @validator("sex")
    def sex_valid(cls, v):
        if v not in ["Male", "Female", "Other"]:
            raise ValueError("Sex must be Male, Female, or Other")
        return v


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AdminOTPVerifyRequest(BaseModel):
    email: EmailStr
    otp_code: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str