from aiogram import types, Bot

class Mailing:

    def __init__(self, m: types.Message, bot: Bot, users: list, admin_id: int):
        self.m = m
        self.bot = bot
        self.users_list = users
        self.admin = admin_id

        self.success = 0
        self.errors = 0

    async def run(self):

        for user in self.users_list:
            try:
                await self.bot.copy_message(chat_id=user, from_chat_id=self.admin, message_id=self.m.message_id, reply_markup=self.m.reply_markup)
                print(self.m.text, user)
                self.success += 1
            except Exception:
                self.errors += 1

        await self.__notify_admin()

    async def __notify_admin(self):
        await self.bot.send_message(chat_id=self.admin, text=f"Рассылка завершена!\nУспешно отправлено: {self.success}\nОшибок: {self.errors}")

