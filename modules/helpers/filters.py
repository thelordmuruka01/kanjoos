from typing import Union, List
from pyrogram import filters
from modules.config import COMMAND_PREFIXES, SUDO_USERS

# Basic chat type filters
other_filters = (
    filters.group
    & ~filters.via_bot
    & ~filters.forwarded
)
# Add a filter that only allows SUDO users
sudo_filter = filters.user(SUDO_USERS)

def command(commands: Union[str, List[str]]):
    # This automatically uses the prefixes from your config
    return filters.command(commands, COMMAND_PREFIXES)
