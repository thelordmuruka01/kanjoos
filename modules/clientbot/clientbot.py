from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types import MediaStream
from modules import config
from . import queues

client = Client(config.STRING_SESSION, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.play(
    chat_id,
    MediaStream(
        queues.get(chat_id)["file"],
    ),
)
      
run = pytgcalls.start
async def run():
    async with aiohttp.ClientSession() as session:
        # Pass this session to parts of your app that need it
        await start_bot(session)
