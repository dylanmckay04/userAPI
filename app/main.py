from fastapi import FastAPI
from app.database import Base, engine
from app.models import user
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return{"status": "ok"}
