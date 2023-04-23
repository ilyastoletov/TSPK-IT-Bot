from aiogram import Router, types
from filters.admin_filter import AdminFilter
from aiogram.filters.text import Text
from keyboards.default import cancel_keyboard, admin_keyboard
from aiogram.fsm.context import FSMContext
from states.admin import AdminStates
from database.main import Database

r = Router()
r.message.filter(AdminFilter())

@r.message(Text("➕ Добавить вопрос"))
async def add_question(m: types.Message, state: FSMContext):
    await m.answer("Введите текст вопроса, который хотите добавить", reply_markup=cancel_keyboard())
    await state.set_state(AdminStates.add_question)

@r.message(AdminStates.add_question)
async def add_answer(m: types.Message, state: FSMContext):
    await state.update_data(data={'question' : m.text})
    await m.answer("Теперь напишите ответ на этот вопрос")
    await state.set_state(AdminStates.add_answer)

@r.message(AdminStates.add_answer)
async def answer_added(m: types.Message, state: FSMContext, db: Database):
    question = (await state.get_data())['question']
    try:
        await db.add_question_object(question, m.text)
    except Exception as e:
        await m.answer(f"Произошла ошибка {e}")
    await m.answer("Вопрос успешно добавлен!", reply_markup=admin_keyboard())

