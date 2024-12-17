from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from tokens.dependencies import does_token_exist
from tokens.service import add_session

router = APIRouter()


@router.get("/token")
async def get_token(response: Response, token: Annotated[bool, Depends(does_token_exist)]):
    if not token:
        raise HTTPException(status_code=401, detail="This token does not have permissions")
    session = add_session(token)
    response.set_cookie("session_id", value=session, httponly=True)
    return {"message":"Token used successfully"}

    
@router.post("/token")
async def create_token(session_id: Annotated[str | None, Cookie()] = None):  
    pass



@router.delete("/token")
async def delete_token():
    pass
