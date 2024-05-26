import asyncio
from app.core.config import settings
from app.core.database import create_engine, Base

async def init_db():
    engine = create_engine(settings.DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
