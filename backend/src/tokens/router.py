from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response
from tokens.dependencies import does_token_exist, is_in_session
from tokens.service import add_session, add_token

router = APIRouter()


@router.get("/token")
async def get_token(response: Response, token: Annotated[bool, Depends(does_token_exist)]):

    if not token:
        raise HTTPException(status_code=401, detail="This token does not have permissions")
    session = add_session(token)
    response.set_cookie("session_id", value=session, httponly=True)
    return {"message":"Session created"}

    
@router.post("/token")
async def create_token(s: Annotated[bool, Depends(is_in_session)] = None):
    return {"new token": add_token()}
    



