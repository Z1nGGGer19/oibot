from urllib3 import response
from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import replykeyboards, inlinekeyboards
from create_bot import bot
from Google_sheets.manager_sheets import get_value_from_sheet
from views import start_view, parser
from database.requests import get_user


start_router = Router()


class CallbackOnStart(StatesGroup):
    Q1 = State()

users = ["yinkahah", "Hashiba1", "Victori1802", "kriingee", "z1ngger19"]

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    link = message.from_user.username
    if link in users:
        await get_user(user_id)
        await message.answer('салаааааамуаллейкум все ждущим тасков',
                         reply_markup=replykeyboards.main_kb())
    else:
        await message.answer('а нахуй сходить не хочешь?) иди плати за доступ🤗')


#вызов ссылки на яндекс карты
@start_router.message(F.text.lower() == 'яндекс карты')
async def call_inline(message: Message):
    image = await start_view.generate_image(967)

    image_path = 'weeks_image.png'
    image.save(image_path)

    with open(image_path, 'rb') as file:
        await bot.send_photo(chat_id=message.chat.id, photo=file)


#вызов ссылки на яндекс карты
@start_router.message(F.text.lower() == 'таски')
async def get_tasks(message: Message):
    link = message.from_user.username
    if not link in users:
        await message.answer('а нахуй сходить не хочешь?) иди плати за доступ🤗')
        return
    data = parser.request_to_tasks()
    tasks = parser.get_list_by_tasks(data)
    await message.answer(tasks,
                         reply_markup=replykeyboards.main_kb())
    
#получение значения из поля А2
@start_router.message(F.text == 'Значение из А2')
async def get_value(message: Message):
    await message.answer(get_value_from_sheet())


#отправка изображения
@start_router.message(F.text.lower() == 'картинка')
async def answer_image(message: Message):
    photo = FSInputFile("путь к картинке")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

#запрос на запись даты
@start_router.message(F.text.lower() == 'внести дату')
async def inp_date(message: Message, state: FSMContext):
    await message.answer('Введите дату')
    await state.set_state(CallbackOnStart.Q1)


#проверка даты на корректность и внос в таблицу
@start_router.message(CallbackOnStart.Q1)
async def write_date(message: types.Message):
    date = message.text
    response = await start_view.input_date(date)
    await message.answer(response)
