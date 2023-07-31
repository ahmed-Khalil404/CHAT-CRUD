from pydantic import BaseModel
from typing import List

class Conversation(BaseModel):
    creator_id: str
    title: str
    group_chat: bool
    members_id: List[str]
