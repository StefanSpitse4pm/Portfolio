from database import Querying
from fastapi import Depends
from typing import Annotated

from models import TokenModel

from sqlalchemy import Select, func


async def get_db():
    db = Querying()
    return db

async def does_token_exist(token: str, db: Annotated[Querying, Depends(get_db)]):
    out = await db.Send(
        Select(func.count())
        .select_from(TokenModel)
        .where(TokenModel.token.in_([token]))
    )
    return {token:out.iloc[0].to_list()[0] >= 1}
