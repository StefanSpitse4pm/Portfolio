from fastapi import FastAPI
from tokens.router import router as tokens_router

app = FastAPI()
app.include_router(tokens_router)

