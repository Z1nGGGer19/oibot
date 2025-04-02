import asyncio
from time import sleep
from . import parser
from database import requests
from create_bot import bot
from Config import config


async def update_tasks():
    while True:
        try:
            print("обнова")
            data = parser.request_to_tasks()
            if not await requests.get_task_count():
                await requests.add_task(0)
                print("добавил в бд")
                continue
            if await requests.get_task() != len(data):
                new_tasks = parser.check_list_of_tasks(data)
                message = parser.get_message(new_tasks)
                await requests.update_first_task_value(len(data))
                for user in await requests.get_users():
                    try:
                        await bot.send_message(user.user_id, message)
                    except Exception as e:
                        print(f"Не удалось отправить сообщение пользователю {user.user_id}: {e}")
            await asyncio.sleep(5)
        except: 
            continue

async def info_message():
    for i in config.ID:
        pass
        # try:
        #     await bot.send_message(i, "Бот был обновлён, для корректной работы пропиши /start")
        # except:
        #     print('нет диалога с юзером')