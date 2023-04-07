from aiogram import Router, types, F
from aiogram.filters.text import Text
from aiogram.filters.command import Command
from keyboards.default import start_menu, entrant_menu, department_choose

r = Router()


@r.message(Command('start'))
async def start_message(m: types.Message):
    await m.answer("Добро пожаловать в бот IT-отделения ТСПК!\nПеред вами основное меню:", reply_markup=start_menu())


@r.message(Text("Абитуриенту"))
async def entrant_menu(m: types.Message):
    await m.answer("Меню абитурента", reply_markup=entrant_menu())


@r.message(Text("Часто задаваемые вопросы"))
async def answer_often_questions(m: types.Message):
    await m.answer(
        "Q: Тестовый вопрос 1?\nA: Тестовый ответ 1\n\nQ: Тестовый вопрос 2?\nA: Тестовый ответ 2\n\nQ: Тестовый вопрос 3?\nA: Тестовый ответ 3\n\n")


@r.message(Text("Подробнее о колледже и IT-отделении"))
async def college_description(m: types.Message):
    await m.answer(
        "Вы поступили в лучший колледж самарской области, россии и вообще мира!1!!1!!\n*дальнейший тест про колледж, ссылки, и т.д*")


@r.message(Text("Чат группы, в которую поступил"))
async def group_chats(m: types.Message):
    await m.answer("Выберите отделение, на которое вы подали документы, или вы уже есть в приказе на зачисление",
                   reply_markup=department_choose())


@r.message(Text(["ИСиП", "КС"]))
async def group_chosen(m: types.Message):
    await m.answer(f"Вот чат абитуриентов отделения {m.text}: *ссылка на чат*")
