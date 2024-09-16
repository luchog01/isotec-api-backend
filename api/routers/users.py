from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.repositories.database import get_db
from api.models.user import UserInDB
from api.controllers.users import UserController
from api.routers.auth import oauth2_scheme

router = APIRouter()

@router.get("/users/me", response_model=UserInDB)
async def read_users_me(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    return await UserController.get_current_user(token, db)