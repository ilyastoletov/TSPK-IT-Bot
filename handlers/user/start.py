from aiogram import types, Router
from keyboards.default import start_menu
from aiogram.filters.command import Command

r = Router()

@r.message(Command('start'))
async def start_message(m: types.Message):
    await m.answer("Добро пожаловать в бот IT-отделения ТСПК!\nПеред вами основное меню:", reply_markup=start_menu())