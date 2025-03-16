from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_kb():
    kb_list = [
        [KeyboardButton(text='Таски')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, 
                                   resize_keyboard=True, 
                                   input_field_placeholder='Выберите пункт меню')

    return keyboard