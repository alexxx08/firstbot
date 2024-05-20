from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Запуск бота'),
        types.BotCommand(command='/help', description='Чем может помочь бот'),
        types.BotCommand(command='/stop', description='Остановить бота'),
        types.BotCommand(command='/link', description='Cсылка на видео'),
        types.BotCommand(command='/photo', description='Фотография'),
        types.BotCommand(command='/translator', description='Ссылка на переводчик')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый бот', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото неба')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://kartinki.pics/uploads/posts/2021-07/1626901824_15-kartinkin-com-p-krasivoe-nebo-tekstura-krasivo-15.jpg', caption= 'Красивое небо')

@dp.message_handler(lambda message: message.text == 'Отправь фото заката')
async def button_2_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://lh5.googleusercontent.com/proxy/-KZIq0Lhl46iD87wrSxUf1SzGgDXU5oar4Wr-bW9_aRVMV7l93hFV3IPK4i7YGsZQAyMrkrlEKJvy38BUBceWBvq0AmNNfoGsIPFkffj0TR_4Tv8IHElSeX4zl8DkmwMybz36LHFhY6Ykw12AyQY1-YVaN5U46ef', caption= 'Красивый закат')

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_3_click(message: types.Message):
    await message.answer('Ты можешь посмотреть животных', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото лисы')
async def button_4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://fbi.cults3d.com/uploaders/25181852/illustration-file/31604d4d-352a-4050-90f2-97fea9c69bc4/Fox-1.png', caption= 'Лиса из майнкрафта')

@dp.message_handler(lambda message: message.text == 'Отправь фото белки')
async def button_5_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://www.shutterstock.com/image-photo/portrait-eurasian-red-squirrel-front-260nw-283837010.jpg', caption= 'Белка')

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_6_click(message: types.Message):
    await message.answer('Ты можешь вернуться', reply_markup= get_keyboard_1())


@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с ...')

@dp.message_handler(commands= 'stop')
async def stop(message: types.Message):
    await message.answer('Прекращаю  свою работу')

@dp.message_handler(commands= 'link')
async def link(message: types.Message):
    await message.reply('https://www.youtube.com/watch?v=WgsipLkCh3c&list=PLBxD0UwW2SxmiogBXtVv5kItQXXQaPPKh&index=3')

@dp.message_handler(commands= 'photo')
async def Photo(message: types.Message):
    await message.answer('https://img.freepik.com/premium-photo/beautiful-sky-with-white-cloud-sky-gradient-background_410516-43650.jpg?w=1380')

@dp.message_handler(commands= 'translator')
async def translator(message: types.Message):
    await message.answer('https://translate.google.com/?hl=ru&sl=auto&tl=en&op=translate')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
