from aiogram import Router, types, Bot
from keyboards.default import admin_keyboard
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from filters.admin_filter import AdminFilter
from aiogram.fsm.context import FSMContext

r = Router()
r.message.filter(AdminFilter())

@r.message(Command("admin"))
async def admin_menu_show(m: types.Message):
    await m.answer("Добро пожаловать в админ меню", reply_markup=admin_keyboard())

@r.message(Text("Отмена"))
async def cancel_action(m: types.Message, state: FSMContext):
    await m.answer("Действие отменено", reply_markup=admin_keyboard())
    await state.clear()
