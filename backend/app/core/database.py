from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,          # Turn off in production — stops printing every SQL query
    future=True,
    pool_size=5,         # Keep 5 connections open at all times
    max_overflow=10,     # Allow 10 extra connections if needed
    pool_timeout=30,     # Wait max 30 seconds for a connection
    pool_recycle=1800,   # Recycle connections every 30 minutes
    pool_pre_ping=True,  # Check connection is alive before using it
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()