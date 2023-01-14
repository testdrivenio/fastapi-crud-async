from app.api.models import NoteSchema
from app.db import notes, async_session


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    
    with async_session() as db:
        response = await db.execute(query=query)

    return response 


async def get(id: int):
    query = notes.select().where(id == notes.c.id)

    with async_session() as db:
        response = await db.execute(query=query)
        
    return response 


async def get_all():
    query = notes.select()
    with async_session() as db:
        response = await db.execute(query=query)
        
    return response 


async def put(id: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )

    with async_session() as db:
        response = await db.execute(query=query)
        
    return response 


async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)

    with async_session() as db:
        response = await db.execute(query=query)
        
    return response 
