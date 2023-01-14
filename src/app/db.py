import os

import logging
logger = logging.getLogger(__name__)
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL").replace('postgresql', 'postgresql+asyncpg')
logger.debug(DATABASE_URL, 'DATABASE_URL')

# SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# sessionmaker version
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)