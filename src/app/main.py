import asyncio
from fastapi import FastAPI

from app.api import notes, ping
from app.db import engine, metadata


"""async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    
    await engine.dispose()

asyncio.run(async_main())"""


app = FastAPI()


@app.on_event("startup")
async def startup():
    await engine.connect()


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
