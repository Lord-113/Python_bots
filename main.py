from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from nekot import *
import linecache, random

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь') # поменять


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        '/what_do_you_do \n'
        '/hello_world'
    )

@dp.message(Command(commands=['hello_world']))
async def process_hello_world_command(message: Message):
    await message.answer(
        'Привет мир!'
    )
@dp.message(Command(commands=['what_do_you_do']))
async def process_what_do_you_do_command(message: Message):
    await message.answer(
        'Я существую чтобы написать "Привет мир!"'
    )

@dp.message(Command(commands=['generate']))
async def generate(message: Message):
    await message.answer(
        linecache.getline("surnames.txt", random.randint(1,14650))
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
