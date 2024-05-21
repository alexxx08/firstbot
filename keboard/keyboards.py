from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard1 = InlineKeyboardMarkup(row_width= 1)
button1 = InlineKeyboardButton('Переключиться на Котиков', callback_data= 'go_to_1')
button2 = InlineKeyboardButton('Переключиться на Собак', callback_data= 'go_to_2')
button3 = InlineKeyboardButton('Переключиться на Пингвинов', callback_data= 'go_to_3')
keyboard1.add(button1, button2, button3)

keyboard2 = InlineKeyboardMarkup(row_width= 1)
button4 = InlineKeyboardButton('Переключиться на Собак', callback_data= 'go_to_2')
button5 = InlineKeyboardButton('Переключиться на Пингвинов', callback_data= 'go_to_3')
button6 = InlineKeyboardButton('Переключиться на Главную', callback_data= 'go_to_0')
keyboard2.add( button4, button5, button6)

keyboard3 = InlineKeyboardMarkup(row_width= 1)
button7 = InlineKeyboardButton('Переключиться на Котиков', callback_data= 'go_to_1')
button8 = InlineKeyboardButton('Переключиться на Пингвинов', callback_data= 'go_to_3')
button9 = InlineKeyboardButton('Переключиться на Главную', callback_data= 'go_to_0')
keyboard3.add(button7, button8, button9)

keyboard4 = InlineKeyboardMarkup(row_width= 1)
button10 = InlineKeyboardButton('Переключиться на Котиков', callback_data= 'go_to_1')
button11 = InlineKeyboardButton('Переключиться на Собак', callback_data= 'go_to_2')
button12 = InlineKeyboardButton('Переключиться на Главную', callback_data= 'go_to_0')
keyboard4.add(button10, button11, button12)