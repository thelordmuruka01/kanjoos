```python
from typing import Union, List
from pyrogram import filters
from modules.config import COMMAND_PREFIXES

other_filters = (
    filters.group
    & ~filters.via_bot
    & ~filters.forwarded
)


# Standard command handler
def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)


# Premium/pro command handler compatibility
def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
```
