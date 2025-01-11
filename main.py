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
    await message.answer('Привет!\nНеважно как меня зовут, просто напиши мне что-нибудь!')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        '/what_do_you_do \n'
        '/generate'
    )


@dp.message(Command(commands=['what_do_you_do']))
async def process_what_do_you_do_command(message: Message):
    await message.answer(
        'Я помогаю творческим людам с недостатком фантазии и комбинирую имена и фамилии. \n'
        'Не хочу чтобы вы затрудняли себя этим)  '
    )


@dp.message(Command(commands=['generate']))
async def generate(message: Message):
    await message.answer(
        linecache.getline("names.txt", random.randint(1, 615)).strip() + ' ' +
        linecache.getline("surnames.txt", random.randint(1, 14650))
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд


if __name__ == '__main__':
    dp.run_polling(bot)
