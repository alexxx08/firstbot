from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import keyboard1, keyboard2, keyboard3, keyboard4
from database.database import initialize_dp, add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_dp()


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
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.reply('Есть несколько вариантов картинок: ', reply_markup= keyboard1)
    else:
        await message.reply('Есть несколько вариантов картинок: ', reply_markup=keyboard1)

@dp.callback_query_handler(lambda c: c.data == 'go_to_0')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Есть несколько вариантов картинок: ', reply_markup= keyboard1)


@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    # await callback_query.message.edit_text('Котики', reply_markup= keyboard2)
    await bot.send_photo(callback_query.from_user.id, photo= 'https://prochepetsk.ru/userfiles/picfullsize/image-1677667806_9146.jpg', caption= 'Кошка', reply_markup= keyboard1)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    # await callback_query.message.edit_text('Собаки', reply_markup= keyboard3)
    await bot.send_photo(callback_query.from_user.id, photo='https://storage.yandexcloud.net/storage.yasno.media/nat-geo/images/2023/6/28/a9c7c5ba9c2e4caa9330c1ec5c0fc499.max-2000x1000.jpg', caption= 'Собака', reply_markup= keyboard1)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
@dp.callback_query_handler(lambda c: c.data == 'go_to_3')
async def go_to_3(callback_query: types.CallbackQuery):
    # await callback_query.message.edit_text('Пингвины', reply_markup= keyboard4)
    await bot.send_photo(callback_query.from_user.id, photo='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Emperor_penguin.jpg/273px-Emperor_penguin.jpg', caption= 'Пингвин', reply_markup= keyboard1)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
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
