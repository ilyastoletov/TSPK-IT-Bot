from aiogram.fsm.state import State, StatesGroup

class AdminStates(StatesGroup):
    add_question = State()
    add_answer = State()
    post = State()