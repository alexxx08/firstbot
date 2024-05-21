from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Про облака', url='https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D0%BB%D0%B0%D0%BA%D0%B0')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline2():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline2 = InlineKeyboardButton('Про закаты', url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%B0%D1%82')
    keyboard_inline.add(but_inline2)
    return keyboard_inline

def get_keyboard_inline3():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline3 = InlineKeyboardButton('Про лис', url='https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%81%D0%B8%D1%86%D0%B0')
    but_inline4 = InlineKeyboardButton('Лиса из майнкрафта', url='https://minecraft.fandom.com/ru/wiki/%D0%9B%D0%B8%D1%81%D0%B0#:~:text=%D0%9B%D0%B8%D1%81%D1%8B%20%D0%B2%D0%B5%D0%B4%D1%83%D1%82%20%D0%BD%D0%BE%D1%87%D0%BD%D0%BE%D0%B9%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%20%D0%B6%D0%B8%D0%B7%D0%BD%D0%B8,%D0%B8%D0%B3%D1%80%D0%BE%D0%BA%20%D0%BF%D1%80%D0%B8%D0%B1%D0%BB%D0%B8%D0%B6%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D0%BA%20%D0%BD%D0%B8%D0%BC%20%D0%BF%D0%BE%D0%B4%D0%BA%D1%80%D0%B0%D0%B4%D1%8B%D0%B2%D0%B0%D1%8F%D1%81%D1%8C.')
    keyboard_inline.add(but_inline3, but_inline4)
    return keyboard_inline