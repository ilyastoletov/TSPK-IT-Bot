from aiogram import Router, types, Bot
from aiogram.filters.text import Text
from filters.admin_filter import AdminFilter
from aiogram.fsm.context import FSMContext
from database.main import Database
from states.admin import AdminStates
from keyboards.default import cancel_keyboard, admin_keyboard
from util.mail import Mailing
from keyboards.inline import post_confirmation_keyboard

r = Router()
r.message.filter(AdminFilter())

@r.message(Text("📤 Рассылка"))
async def post_message(m: types.Message, state: FSMContext):
    await m.answer("Пришлите сообщение для рассылки. Допускаются все виды контента, кроме альбомов", reply_markup=cancel_keyboard())
    await state.set_state(AdminStates.post)

@r.message(AdminStates.post)
async def post_confirm(m: types.Message, state: FSMContext):
    await state.update_data(data={'message' : m})
    await m.answer("Контент получен. Запускаем?", reply_markup=post_confirmation_keyboard())

@r.callback_query(Text(startswith="post_"))
async def post_got_decision(c: types.CallbackQuery, bot: Bot, db: Database, state: FSMContext):
    decision = c.data.split("_")[1]
    users_list = await db.fetch_all_users()
    message = (await state.get_data())['message']
    mail = Mailing(m=message, bot=bot, admin_id=c.from_user.id, users=users_list)

    if decision == 'confirm':
        await c.message.delete()
        await c.message.answer("Рассылка запущена!\nРезультаты придут сюда после ее завершения", reply_markup=admin_keyboard())
        await state.clear()
        await mail.run()
    else:
        await c.message.delete()
        await c.message.answer("Рассылка отменена", reply_markup=admin_keyboard())
        await state.clear()
