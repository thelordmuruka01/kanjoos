from typing import Union, List
from pyrogram import filters
from modules.config import COMMAND_PREFIXES

other_filters = (
    filters.group
    & ~filters.via_bot
    & ~filters.forwarded
)

# 3. Standard Command (uses / or !)
def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
