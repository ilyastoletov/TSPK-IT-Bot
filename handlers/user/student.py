from aiogram import Router, types
from aiogram.filters.text import Text
from keyboards.default import start_menu, student_menu
from keyboards.inline import question_choosing, back_to_choose

r = Router()


@r.message(Text("Студенту"))
async def entrant_menu(m: types.Message):
    await m.answer("Меню студента", reply_markup=student_menu())

@r.message(Text("Расписание"))
async def college_schedule(m: types.Message):
    await m.answer("Актуальное расписание всегда доступно в telegram-боте @tspc_schedule_bot")

@r.message(Text("Задать вопрос"))
async def ask_question_choose_category(m: types.Message):
    await m.answer("Выберите характер своего вопроса", reply_markup=question_choosing())

@r.callback_query(Text(startswith="help_"))
async def question_helper_suggest(c: types.CallbackQuery):
    question_category = c.data.split("_")[1]
    helper_link = ""

    if question_category == "finance":
        helper_link = "@wr479"
    elif question_category == "studying":
        helper_link = "@risely"
    elif question_category == "non-study":
        helper_link = "@durov"

    await c.message.edit_text(f"Напишите этому человеку и подробно опишите свой вопрос: {helper_link}", reply_markup=back_to_choose('help'))

@r.callback_query(Text("help-back-to-choose"))
async def back_to_choosing(c: types.CallbackQuery):
    await c.message.edit_text("Выберите характер своего вопроса", reply_markup=question_choosing())