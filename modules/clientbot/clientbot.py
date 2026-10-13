from pyrogram import Client
from pytgcalls import PyTgCalls, filters
from pytgcalls.types import StreamEnded, MediaStream
from modules import config
from . import queues

client = Client(config.STRING_SESSION, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_update(filters.stream_end())
async def on_stream_end(_: PyTgCalls, update: StreamEnded):
    chat_id = update.chat_id

    next_song = queues.get(chat_id)

    if next_song and next_song.get("file"):
        try:
            await pytgcalls.play(
                chat_id,
                MediaStream(next_song["file"]),
            )
            queues.task_done(chat_id)
        except Exception as e:
            print(f"Autoplay error in chat {chat_id}: {e}")
            await pytgcalls.leave_call(chat_id)
    else:
        await pytgcalls.leave_call(chat_id)

      
async def run():
    await pytgcalls.start()
