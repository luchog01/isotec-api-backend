from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from api.repositories.database import get_db
from api.models.user import UserCreate
from api.controllers.auth import AuthController
from api.utils.logger import api_logger


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    response = await AuthController.register(user, db)
    api_logger.info(f"User {response.email} registered")
    return response

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    response = await AuthController.login(form_data.username, form_data.password, db)
    api_logger.info(f"User {form_data.username} logged in")
    return response