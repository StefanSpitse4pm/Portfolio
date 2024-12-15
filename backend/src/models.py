from datetime import datetime

from sqlalchemy import VARCHAR, DateTime, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class TokenModel(Base):
    __tablename__ = "tokens"
    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(VARCHAR(255))
    
    session = relationship("Session", back_populates="token", cascade="all, delete-orphan")

class Session(Base):
    __tablename__ = "session"
    id: Mapped[int] = mapped_column(primary_key=True)
    session: Mapped[str] = mapped_column(VARCHAR(20))
    token_id: Mapped[int] = mapped_column(Integer, ForeignKey('tokens.id'), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime)

    token = relationship("TokenModel", back_populates="session")
