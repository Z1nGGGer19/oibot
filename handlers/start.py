from ast import arg
from urllib import response
from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import replykeyboards
from create_bot import bot
from views import parser
from database.requests import get_user
from Config import config

start_router = Router()


class CallbackOnStart(StatesGroup):
    Q1 = State()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    link = message.from_user.username
    if link in config.LINKS:
        await get_user(user_id)
        await message.answer('ёбаный баклажан',
                             reply_markup=replykeyboards.main_kb())
    else:
        await message.answer('а нахуй сходить не хочешь?) иди плати за доступ🤗')


# вызов ссылки на яндекс карты
@start_router.message(F.text.lower() == 'таски')
async def get_tasks(message: Message):
    link = message.from_user.username
    if not link in config.LINKS:
        await message.answer('а нахуй сходить не хочешь?) иди плати за доступ🤗')
        return
    data = parser.request_to_tasks()
    tasks = parser.get_list_by_tasks(data)
    await message.answer(tasks,
                         reply_markup=replykeyboards.main_kb())


@start_router.message(Command('ahtung'))
async def ahtung(message: Message, command: CommandObject):
    if message.from_user.username != 'l0cal_host':
        return
    args = command.args.split(maxsplit=1)
    if message.photo:
        file_id = message.photo[-1].file_id
        await bot.send_photo(int(args[0]), photo=file_id)
    await bot.send_message(int(args[0]), text=args[1])