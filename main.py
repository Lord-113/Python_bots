from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from nekot import *
from funsctions_to_import import *

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
    builder = InlineKeyboardBuilder()
    builder.button(text="мужской", callback_data="option_male")
    builder.button(text="женский", callback_data="option_female")
    await message.answer(
        'Выберите пол', reply_markup=builder.as_markup()
    )


@dp.callback_query()
async def name_callback(callback_query: CallbackQuery):
    if callback_query.data == "option_male":
        await callback_query.message.answer(
            f"Вы выбрали мужское имя и фамилию, продолжаю процесс генерации...\n{gen_male()}")
    elif callback_query.data == "option_female":
        await callback_query.message.answer(
            f"Вы выбрали женское имя и фамилию, продолжаю процесс генерации...\n{gen_female()}")


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд
@dp.message()
async def echo(message: Message):
    print(message.text)
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
