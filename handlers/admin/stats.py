from aiogram import Router, types
from database.main import Database
from aiogram.filters.text import Text
from filters.admin_filter import AdminFilter

r = Router()
r.message.filter(AdminFilter())

@r.message(Text("📊 Статистика"))
async def show_stats(m: types.Message, db: Database):
    user_stats = await db.fetch_user_stats()
    alive = int(user_stats['all']) - int(user_stats['blocked'])
    await m.answer(f"Статистика бота <b>IT ТСПК</b>\n\nВсего юзеров: {user_stats['all']}\nЖивые: {alive}\nМертвые: {user_stats['blocked']}")
