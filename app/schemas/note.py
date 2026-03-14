from pydantic import BaseModel, field_validator
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    body: str
    
    @field_validator("title")
    @classmethod
    def title_must_be_valid(cls, v):
        if not v.strip():
            raise ValueError("Title cannot be blank")
        if len(v) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        return v.strip()
    
    @field_validator("body")
    @classmethod
    def title_must_be_valid(cls, v):
        if not v.strip():
            raise ValueError("Body cannot be blank")
        if len(v) > 10000:
            raise ValueError("Body cannot exceed 10000 characters")
        return v.strip()

class NoteOut(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    owner_id: int
    
    class Config:
        from_attributes = True