from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

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
    await message.answer('Привет, я твой первый бот')

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
