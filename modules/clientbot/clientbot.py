from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types import MediaStream
from modules import config
from . import queues

client = Client(config.STRING_SESSION, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_update(filters.stream_end())
async def on_stream_end(_: PyTgCalls, update: StreamEnded):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_call(chat_id)
    else:
        next_song = queues.get(chat_id)
        if next_song:
            await pytgcalls.play(
                chat_id,
                MediaStream(next_song["file"]),
            )
      
async def run():
    await pytgcalls.start()
