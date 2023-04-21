from aiogram import Router, types
from aiogram.filters.text import Text
from keyboards.inline import clubs_choose_keyboard, back_to_choose
from database.main import Database

r = Router()

@r.message(Text("Клубы"))
async def clubs_list(m: types.Message, db: Database):
    clubs_list = await db.fetch_clubs()
    await m.answer("Вот список всех клубов, которые есть в колледже сейчас. Нажмите на один из них, чтобы увидеть подробную информацию и получить ссылку на вступление в чат клуба и контакт тимлида, если захотите в него вступить",
                   reply_markup=clubs_choose_keyboard(clubs_list)
                   )

@r.callback_query(Text(startswith="clubInfo_"))
async def club_info_reply(c: types.CallbackQuery, db: Database):
    club_name = c.data.split("_")[1]
    club_info = await db.fetch_club_info(club_name)

    await c.message.edit_text(f"{club_info['description']}\n\nТимлид: {club_info['teamlead_link']}\nЧат: {club_info['chat_link']}", reply_markup=back_to_choose('clubs'))

@r.callback_query(Text('clubs-back-to-choose'))
async def back_to_choose_clubs(c: types.CallbackQuery, db: Database):
    await c.message.delete()
    await clubs_list(c.message, db)