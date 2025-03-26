from urllib import response
import requests
from bs4 import BeautifulSoup

from Config import config


CREDENTIALS = {
    "name": "Плескачев Рома",
    "password": "Roma23001025!",
    "_submit": "Войти",
}

def login(session):
    response = session.get(config.LOGIN_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_nonce = soup.find("input", {"name": "nonce"})["value"]
    
    CREDENTIALS["nonce"] = csrf_nonce
    session.post(config.LOGIN_URL, data=CREDENTIALS)

def get_tasks(session):
    response = session.get(config.CHALLENGES_URL)
    return response.json().get('data')


def request_to_tasks():
    session = requests.Session()
    login(session)
    data = get_tasks(session)
    return data

def get_list_by_tasks(data):
    tasks = []
    for task in data:
        tasks.append(f"✅ {task.get('name')}") if task.get('solved_by_me') else tasks.append(f"❌ {task.get('name')}")
    return "\n".join(tasks)

def get_message(new_tasks):
    session = get_session()
    login(session)
    message = 'Таски обновились'
    for i in new_tasks:
        task = get_task_by_id(session, i)
        message += f'\nНазвание: {task.get("name")}\n'
        message += f'Категория: {task.get("category")}\n'
        message += f'Описание: {task.get("description")}\n'
        message += '\n'
    return message
