from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup

def often_questions(questions_list: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for question in questions_list:
        builder.add(
            InlineKeyboardButton(text=question['question'], callback_data=f"question_{question['id']}")
        )
    builder.adjust(1)
    return builder.as_markup()

def clubs_choose_keyboard(clubs_list: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for club in clubs_list:
        builder.add(InlineKeyboardButton(text=club['name'], callback_data=f'clubInfo_{club["name"]}'))
    builder.adjust(1)
    return builder.as_markup()

def question_choosing() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Финансы", callback_data="help_finance"),
        InlineKeyboardButton(text="Обучение", callback_data="help_studying"),
        InlineKeyboardButton(text="Внеучебная деятельность", callback_data="help_non-study"),
        width=1
    )
    return builder.as_markup()

def back_to_choose(topic: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="◀️ Назад", callback_data=f"{topic}-back-to-choose"))
    return builder.as_markup()
