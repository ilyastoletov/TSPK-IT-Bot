from aiogram import types, Router
from keyboards.default import start_menu
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from database.main import Database

r = Router()

@r.message(Command('start'))
async def start_message(m: types.Message, db: Database):
    await m.answer("Добро пожаловать в бот IT-отделения ТСПК!\nПеред вами основное меню:", reply_markup=start_menu())
    await db.create_user(m.from_user.id)

@r.message(Text("◀️ Назад"))
async def back_to_menu(m: types.Message):
    await m.answer("Основное меню", reply_markup=start_menu())