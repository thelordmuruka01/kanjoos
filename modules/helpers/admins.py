from typing import List
from pyrogram.types import Chat
import modules.cache.admins


async def get_administrators(chat: Chat) -> List[int]:
    cached = modules.cache.admins.get(chat.id)

    if cached is not None:
        return cached

    administrators = []

    async for member in chat.get_members(
        filter="administrators"
    ):
        if member.user:
            administrators.append(member.user.id)

    modules.cache.admins.set(chat.id, administrators)

    return administrators
