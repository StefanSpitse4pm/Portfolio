from typing import Annotated

from database import Cache, Querying
from fastapi import Depends
from redis import Redis


async def get_db():
    db = Querying()
    return db

async def does_token_exist(token: str, r: Annotated[Redis, Depends(Cache.make_connection)]):
    return r.get(f"auth:{token}")

