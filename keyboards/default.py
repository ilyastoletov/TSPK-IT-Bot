from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, KeyboardButton

def start_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Абитуренту"),
        KeyboardButton(text="Студенту"),
        KeyboardButton(text="Клубы"),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)

def entrant_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Часто Задаваемые Вопросы"),
        KeyboardButton(text="Подробно о колледже и IT-отделении"),
        KeyboardButton(text="Чат группы, в которую поступил"),
        KeyboardButton(text="◀️ Назад"),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)

def department_choose() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="ИСиП"),
        KeyboardButton(text="КС"),
        width=2
    )
    builder.row(
        KeyboardButton("◀️ Назад"),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)

def student_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Расписание"),
        KeyboardButton(text="Задать вопрос"),
        width=2
    )
    builder.row(
        KeyboardButton("◀️ Назад"),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)