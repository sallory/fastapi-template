from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from src.core.config import db_config


def build_sa_engine() -> AsyncEngine:
    return create_async_engine(
        db_config.database_url,
        pool_size=20,
    )


def build_sa_session_factory(async_engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=async_engine, autoflush=False, expire_on_commit=False)
