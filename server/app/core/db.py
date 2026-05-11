from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from fastapi import Depends

import app.models
from app.core.config import settings

engine = create_async_engine(
    settings.database_url, echo=settings.echo_sql, pool_size=5, max_overflow=10
)


async def get_db_session():
    async with AsyncSession(engine, expire_on_commit=False) as db_session:
        try:
            yield db_session
        except Exception:
            await db_session.rollback()
            raise


AsyncDbSession = Annotated[AsyncSession, Depends(get_db_session)]
