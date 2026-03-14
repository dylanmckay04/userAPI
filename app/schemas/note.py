from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    body: str

class NoteOut(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    owner_id: int
    
    class Config:
        from_attributes = True