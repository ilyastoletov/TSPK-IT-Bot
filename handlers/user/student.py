from aiogram import Router, types
from aiogram.filters.text import Text
from keyboards.default import start_menu, student_menu

r = Router()


@r.message(Text("Студенту"))
async def entrant_menu(m: types.Message):
    await m.answer("Меню студента", reply_markup=student_menu())
