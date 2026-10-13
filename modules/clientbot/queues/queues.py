from asyncio import Queue, QueueEmpty as Empty
from typing import Dict, Optional, Any

queues: Dict[int, Queue] = {}


async def put(chat_id: int, **kwargs) -> int:
    if chat_id not in queues:
        queues[chat_id] = Queue()

    await queues[chat_id].put(dict(kwargs))
    return queues[chat_id].qsize()


def get(chat_id: int) -> Optional[Dict[str, Any]]:
    if chat_id not in queues:
        return None

    try:
        return queues[chat_id].get_nowait()
    except Empty:
        return None


def is_empty(chat_id: int) -> bool:
    return chat_id not in queues or queues[chat_id].empty()


def task_done(chat_id: int) -> None:
    if chat_id in queues:
        try:
            queues[chat_id].task_done()
        except ValueError:
            pass


def clear(chat_id: int) -> None:
    if chat_id not in queues:
        return

    while not queues[chat_id].empty():
        try:
            queues[chat_id].get_nowait()
            queues[chat_id].task_done()
        except Empty:
            break

