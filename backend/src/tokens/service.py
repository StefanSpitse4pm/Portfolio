import secrets
from uuid import uuid4

from database import Cache
from tokens.dependencies import does_token_exist


def add_session(token:str):
    session_token = str(uuid4())
    r = Cache.make_connection()
    r.setex(f"session:{session_token}", 3600, token)
    return session_token

def add_token():
    token = secrets.token_hex(32)
    r = Cache.make_connection()

    two_weeks_in_seconds = 24 * 14 * 60 * 60    
    r.setex(f"auth:{token}", two_weeks_in_seconds, 1)
    if does_token_exist(token):
        return token