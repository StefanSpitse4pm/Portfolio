from uuid import uuid4

from database import Cache


def add_session(token:str):
    session_token = str(uuid4())
    r = Cache.make_connection()
    r.setex(f"session:{session_token}", 3600, token)
    return session_token
    