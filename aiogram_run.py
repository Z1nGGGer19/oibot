import asyncio
from create_bot import bot, dp
from handlers.start import start_router
from database.db import init_db
from views.update_tasks import update_tasks

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await init_db()
    asyncio.create_task(update_tasks())
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')