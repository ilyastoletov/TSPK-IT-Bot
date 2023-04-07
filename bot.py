from aiogram import Dispatcher, Bot
import logging
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.main import r as user_main_handlers
import config

async def admin_notify(bot: Bot):
    await bot.send_message(config.admin, 'Бот запущен')

def register_routers(dp: Dispatcher):
    dp.include_router(user_main_handlers)

async def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(lineno)s - %(name)s - %(message)s')
    logging.error('Starting bot...')
    bot = Bot(token=config.token, parse_mode='HTML')

    dp = Dispatcher(storage=MemoryStorage())

    try:
        register_routers(dp)
        await admin_notify(bot)
        await dp.start_polling(bot)
        logging.error('Bot started!')
    except Exception as e:
        logging.error(f"Bot not started! Error: {e}")
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

def cli():
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')


if __name__ == '__main__':
    cli()
