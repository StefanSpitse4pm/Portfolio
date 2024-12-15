from datetime import datetime, timedelta
from uuid import uuid4

from sqlalchemy import Insert, Select

from models import Session, TokenModel
from tokens.dependencies import get_db


async def add_session(token:str):
    db = await get_db()
    session_token = str(uuid4())
    
    query_get_token_id = Select(TokenModel.id).where(TokenModel.token.in_([token]))
    token_id = await db.Send(query_get_token_id)

    insert_session_query = Insert(Session).values(
            session=session_token,
            token_id=int(token_id.iloc[0]),
            expires_at=datetime.now() + timedelta(weeks=2)
    )
    await db.Send(insert_session_query)
    return session_token
    