from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, Cookie

from tokens.dependencies import does_token_exist
from tokens.service import add_session

router = APIRouter()


@router.get("/token")
async def get_token(response: Response, token: Annotated[dict, Depends(does_token_exist)]):
    if not next(iter(token.values())):
        raise HTTPException(status_code=401, detail="This token does not have permissions")
    session = await add_session(next(iter(token.keys())))
    response.set_cookie("session_id", value=session, httponly=True)
    return {"message":"Token used successfully"}

    
@router.post("/token")
async def create_token(session: str | None = Cookie(default=None)):
    print(session)
    return



@router.delete("/token")
async def delete_token():
    pass
