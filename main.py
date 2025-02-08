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
data = {

}
order = {

}


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nНеважно как меня зовут, просто напиши мне имя!')
    id = message.from_user.id
    if id not in order:
        order[id] = 'name'
    if id not in data:
        data[id] = {}
    print(f'Ваше имя: {id}')


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


@dp.message(Command(commands=['choice_type']))
async def choice_type(message: Message):

    builder = InlineKeyboardBuilder()
    builder.button(text="Русское", callback_data="option_russian")
    builder.button(text="Иностранное", callback_data="option_foreign")
    builder.button(text="Фентезийное", callback_data="option_fantasy")

    await message.answer(
        'Выберите тип имени и фамилии, какое будет имя и фамилия.(Тип будет использоваться для всех следующих генерациях).'
        , reply_markup=builder.as_markup()
    )

@dp.message(Command(commands=['generate']))
async def generate(message: Message):
    id = message.from_user.id
    type = data[id]["type"]
    if type == "russian":
        builder = InlineKeyboardBuilder()
        builder.button(text="мужской", callback_data="option_russ_male")
        builder.button(text="женский", callback_data="option_russ_female")
        await message.answer(
            'Выберите пол', reply_markup=builder.as_markup()
        )
    elif type == "foreign":
        builder = InlineKeyboardBuilder()
        builder.button(text="мужской", callback_data="option_foreign_male")
        builder.button(text="женский", callback_data="option_foreign_female")
        await message.answer(
            'Выберите пол', reply_markup=builder.as_markup()
        )
    elif type == "fantasy":
        builder = InlineKeyboardBuilder()
        builder.button(text="мужской", callback_data="option_fantasy_male")
        builder.button(text="женский", callback_data="option_fantasy_female")
        await message.answer(
            'Выберите пол', reply_markup=builder.as_markup()
        )



@dp.callback_query()
async def name_callback(callback_query: CallbackQuery):
    await callback_query.answer()
    id = callback_query.from_user.id
    if callback_query.data == "option_russ_male":
        await callback_query.message.answer(
            f"Вы выбрали мужское имя и фамилию, продолжаю процесс генерации...\n{gen_russ_male()}")
    elif callback_query.data == "option_russ_female":
        await callback_query.message.answer(
            f"Вы выбрали женское имя и фамилию, продолжаю процесс генерации...\n{gen_russ_female()}")
    elif callback_query.data == "option_foreign_male":
        await callback_query.message.answer(
            f"Вы выбрали мужское имя и фамилию, продолжаю процесс генерации...\n{gen_foreign_male()}")
    elif callback_query.data == "option_foreign_female":
        await callback_query.message.answer(
            f"Вы выбрали женское имя и фамилию, продолжаю процесс генерации...\n{gen_foreign_female()}")
    elif callback_query.data == "option_fantasy_male":
        await callback_query.message.answer(
            f"Вы выбрали мужское имя и фамилию, продолжаю процесс генерации...\n{gen_fantasy_male()}")
    if callback_query.data == "option_russian":
        data[id]["type"] = "russian"
        await callback_query.message.answer("Вы выбрали русский тип имени и фамилии.")
    elif callback_query.data == "option_foreign":
        data[id]["type"] = "foreign"
        await callback_query.message.answer("Вы выбрали иностранный тип имени и фамилии.")
    elif callback_query.data == "option_fantasy":
        data[id]["type"] = "fantasy"
        await callback_query.message.answer("Вы выбрали фентезийный тип имени и фамилии.")


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд
@dp.message()
async def echo(message: Message):
    id = message.from_user.id
    print(message.text)
    if id in data:
        if order[id] == "name":
            data[id][order[id]] = message.text
            order[id] = 'surname'
            await message.answer('Напишите вашу фамилию')
        elif order[id] == 'surname':
            data[id][order[id]] = message.text
            order[id] = None
            await message.answer(f"Имя и фамилия успешно записаны.Вот они: {data[id]['name'], data[id]['surname']}")
    else:
        await message.reply(text=message.text)
    print(data)


if __name__ == '__main__':
    dp.run_polling(bot)
