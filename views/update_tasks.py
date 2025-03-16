import asyncio
from time import sleep
from . import parser
from database import requests
from create_bot import bot


async def update_tasks():
    while True:
        print("обнова")
        data = parser.request_to_tasks()
        if not await requests.get_task_count():
            await requests.add_task(0)
            print("добавил в бд")
            continue
        
        if await requests.get_task() != len(data):
            tasks = parser.get_list_by_tasks(data)
            await requests.update_first_task_value(len(data))
            for user in await requests.get_users():
                try:
                    await bot.send_message(user.user_id, f"Таски обновились!\n{tasks}")
                except Exception as e:
                    print(f"Не удалось отправить сообщение пользователю {user.user_id}: {e}")
        await asyncio.sleep(5)