from aiogram.filters import BaseFilter
from typing import Union
from aiogram import types
import config

class AdminFilter(BaseFilter):

    async def __call__(self, event: Union[types.Message, types.CallbackQuery]) -> bool:
        return event.from_user.id in config.admin