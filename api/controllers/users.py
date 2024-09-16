from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.repositories.users import UserRepository
from jose import jwt, JWTError

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

class UserController:
    @staticmethod
    async def get_current_user(token: str, db: AsyncSession):
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = await UserRepository.get_user_by_email(db, email)
        if user is None:
            raise credentials_exception
        return user