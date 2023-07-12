from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from src.core.config import settings


def build_sa_engine() -> AsyncEngine:
    return create_async_engine(
        settings.database_url,
        pool_size=20,
    )


def build_sa_session_factory(async_engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=async_engine, autoflush=False, expire_on_commit=False)
