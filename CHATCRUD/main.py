from fastapi import FastAPI
from routes.conversation_route import chat_router


app = FastAPI()
app.include_router(chat_router)

