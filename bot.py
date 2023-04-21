from aiogram import Dispatcher, Bot
import logging
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
import config
from database.main import Database
import asyncpg

async def admin_notify(bot: Bot):
    await bot.send_message(config.admin, 'Бот запущен')

def register_routers(dp: Dispatcher):
    from handlers.user.start import r as start_router
    from handlers.user.entrant import r as entrant_router
    from handlers.user.student import r as student_router
    from handlers.user.clubs import r as clubs_router

    dp.include_router(start_router)
    dp.include_router(entrant_router)
    dp.include_router(student_router)
    dp.include_router(clubs_router)

async def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(lineno)s - %(name)s - %(message)s')
    logging.error('Starting bot...')
    bot = Bot(token=config.token, parse_mode='HTML')

    pool = await asyncpg.create_pool(host=config.host,
                               user=config.user,
                               password=config.password,
                               database=config.db_name)
    db = Database(pool=pool)
    dp = Dispatcher(storage=MemoryStorage())
    dp['db'] = db

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
