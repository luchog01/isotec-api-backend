from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.user import User, UserCreate

class UserRepository:
    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str):
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalar_one_or_none()

    @staticmethod
    async def create_user(db: AsyncSession, user_create: UserCreate):
        db_user = User(**user_create.model_dump())
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user