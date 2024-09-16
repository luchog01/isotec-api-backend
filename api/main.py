from fastapi import FastAPI
from api.routers import auth, users
from api.repositories.database import create_all
from api.utils.logger import api_logger  # Import the custom logger

app = FastAPI()

@app.on_event("startup")
async def startup():
    api_logger.info("Starting up the application")
    await create_all()

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    api_logger.info("Root endpoint accessed")
    return {"message": "Welcome to the API"}