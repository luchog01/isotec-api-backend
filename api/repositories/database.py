import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from api.models.user import Base
from api.utils.logger import api_logger

# Create the 'data' directory inside the 'api' folder if it doesn't exist
api_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(api_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

# Update the database path
DATABASE_URL = f"sqlite+aiosqlite:///{os.path.join(data_dir, 'app.db')}"

api_logger.info(f"Database path: {DATABASE_URL}")

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    api_logger.info("Database tables created")

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session