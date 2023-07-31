from fastapi import APIRouter
from models.conversation_model import Conversation
from config.database import collection_name
from schemas.conversation_schema import conversations_serializer, conversation_serializer
from bson import ObjectId

chat_router = APIRouter()


@chat_router.get("/")
async def get_conversation():
    conversations = conversations_serializer(collection_name.find())
    return conversations
@chat_router.get("/{id}")
async def get_conversation(id: str):
    return conversations_serializer(collection_name.find_one({"_id": ObjectId(id)}))
@chat_router.post("/")
async def create_conversation(conversation: Conversation):
    _id = collection_name.insert_one(dict(conversation))
    return conversations_serializer(collection_name.find({"_id": _id.inserted_id}))
@chat_router.put("/{id}")
async def update_conversation(id: str, conversation: Conversation):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(conversation)
    })
    return conversations_serializer(collection_name.find({"_id": ObjectId(id)}))
@chat_router.delete("/{id}")
async def delete_conversation(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}