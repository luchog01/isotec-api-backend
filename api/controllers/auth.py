from sqlalchemy.ext.asyncio import AsyncSession
from api.models.user import UserCreate
from api.exceptions.custom_exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
from api.repositories.users import UserRepository
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthController:
    @staticmethod
    async def register(user: UserCreate, db: AsyncSession):
        db_user = await UserRepository.get_user_by_email(db, user.email)
        if db_user:
            raise EmailAlreadyRegisteredError(db_user.email)
        user.password = pwd_context.hash(user.password)
        return await UserRepository.create_user(db, user)

    @staticmethod
    async def login(email: str, password: str, db: AsyncSession):
        user = await UserRepository.get_user_by_email(db, email)
        if not user or not pwd_context.verify(password, user.password):
            raise InvalidCredentialsError()
        access_token = AuthController.create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)