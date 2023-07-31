def conversation_serializer(conversation) -> dict:
    return {
        "id": str(conversation["_id"]),
        "creator_id": conversation["creator_id"],
        "title": conversation["title"],
        "group_chat": conversation["group_chat"],
        "members_id": conversation["members_id"],
    }

def conversations_serializer(conversations) -> list:
    return [conversation_serializer(conversation) for conversation in conversations]