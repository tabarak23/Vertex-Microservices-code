from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Request DTO (used for POST /users)
class UserCreateRequest(BaseModel):
    email: EmailStr
    name: str


# Response DTO (used for API responses)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # REQUIRED for SQLAlchemy ORM

