from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, KeyboardButton

def start_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Абитуриенту"),
        KeyboardButton(text="Студенту"),
        width=2
    )
    builder.row(
        KeyboardButton(text="Клубы"),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)

def entrant_menu_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Часто Задаваемые Вопросы"),
        KeyboardButton(text="Подробнее о колледже и IT-отделении"),
        KeyboardButton(text="Чат отделения, в которое поступил"),
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
        KeyboardButton(text="◀️ Назад"),
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
        KeyboardButton(text="◀️ Назад"),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)

def admin_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="➕ Добавить вопрос"),
                KeyboardButton(text="📊 Статистика"),
                width=2)
    builder.row(
        KeyboardButton(text="📤 Рассылка"),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)

def cancel_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Отмена"))
    return builder.as_markup(resize_keyboard=True)