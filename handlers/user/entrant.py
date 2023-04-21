from aiogram import Router, types, F
from aiogram.filters.text import Text
from aiogram.filters.command import Command
from keyboards.default import start_menu, entrant_menu_kb, department_choose
from database.main import Database
from keyboards.inline import often_questions, back_to_choose

r = Router()

@r.message(Text("Абитуриенту"))
async def entrant_menu(m: types.Message):
    await m.answer("Меню абитурента", reply_markup=entrant_menu_kb())


@r.message(Text("Часто Задаваемые Вопросы"))
async def answer_often_questions(m: types.Message, db: Database):
    questions_list = await db.fetch_questions()
    await m.answer("Выберите вопрос который вас интересует", reply_markup=often_questions(questions_list))


@r.message(Text("Подробнее о колледже и IT-отделении"))
async def college_description(m: types.Message):
    await m.answer(
        "Вы поступили в лучший колледж самарской области, россии и вообще мира!1!!1!!\n*дальнейший тест про колледж, ссылки, и т.д*")


@r.message(Text("Чат отделения, в которое поступил"))
async def group_chats(m: types.Message):
    await m.answer("Выберите отделение, на которое вы подали документы, или вы уже есть в приказе на зачисление",
                   reply_markup=department_choose())


@r.message(Text(["ИСиП", "КС"]))
async def group_chosen(m: types.Message):
    await m.answer(f"Вот чат абитуриентов отделения {m.text}: *ссылка на чат*")

@r.callback_query(Text(startswith="question_"))
async def question_answer(c: types.CallbackQuery, db: Database):
    question_id = c.data.split("_")[1]
    question_info = await db.fetch_question_info_by_id(int(question_id))
    await c.message.edit_text(f"Вопрос: {question_info['question']}\nОтвет: {question_info['answer']}",
                              reply_markup=back_to_choose('questions'))

@r.callback_query(Text('questions-back-to-choose'))
async def questions_return_to_choosing(c: types.CallbackQuery, db: Database):
    await c.message.delete()
    await answer_often_questions(c.message, db)