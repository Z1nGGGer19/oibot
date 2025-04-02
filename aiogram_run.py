import asyncio
from create_bot import bot, dp
from handlers.start import start_router
from database.db import init_db
from views.update_tasks import update_tasks, info_message


async def main():
    await bot.send_message(chat_id=-1002401240074, text="Бот работает")
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await init_db()
    await info_message()
    asyncio.create_task(update_tasks())
    await dp.start_polling(bot)




if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')