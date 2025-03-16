from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#клавиатура для ссылки на карту
def yandex_map_inline():
    kb = [
        [InlineKeyboardButton(text='Карта', url='https://yandex.ru/maps/-/CDGNJXOV')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


#клавиатура для ссылки на оплату
def url_bill_inline(url: str):
    kb = [
        [InlineKeyboardButton(text='Оплатить', url=url)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)