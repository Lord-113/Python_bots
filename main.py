import json

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandObject
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

with open("data.json", "r") as dt:
    data = json.load(dt)
data = {int(id): data[id] for id in data}
print(data)
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\n'
                         'Я помогаю творческим людам с недостатком фантазии и комбинирую имена и фамилии. \n'
                         'Не хочу чтобы вы затрудняли себя этим). Советую для начала вызвать команду /help  ')
    id = message.from_user.id
    if id not in data:
        data[id] = {"type": "russian", 'favorite': []}
    print(f'Ваше имя: {id}')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        '/help - вызвать это сообщение \n'
        '/choose_type - выбрать тип имени и фамили, пример: русское, иностранное и т.д. (Изначальное значение - русские имена и фамилии) \n'
        '/generate - вызвать команду генерации имени и фамилии \n'
        '/favorite - вызвать список избранных имен \n'
        '/clean_favorite - очистить список избранных.'
    )


@dp.message(Command(commands=['choose_type']))
async def choose_type(message: Message):
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

    if id not in data:
        data[id] = {"type": "russian", 'favorite': []}
    type = data[id]["type"]

    name = message.from_user.full_name
    data[id]["name"] = name
    username = message.from_user.username
    data[id]["username"] = username
    with open("data.json", "w") as dt:
        json.dump(data, dt)

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


@dp.callback_query(lambda c:c.data.startswith("option"))
async def name_callback(callback_query: CallbackQuery):
    await callback_query.answer()
    id = callback_query.from_user.id
    if id not in data:
        data[id] = {"type": "russian", 'favorite': []}
    if callback_query.data == "option_russ_male":
        response = gen_russ_male()
        builder = InlineKeyboardBuilder()
        builder.button(text="в избранное", callback_data=f"favorite_{response}")
        await callback_query.message.answer(
            f"Вы выбрали мужское имя и фамилию, продолжаю процесс генерации...\n{response}",reply_markup = builder.as_markup())

    elif callback_query.data == "option_russ_female":
        response = gen_russ_female()
        builder = InlineKeyboardBuilder()
        builder.button(text="в избранное", callback_data=f"favorite_{response}")
        await callback_query.message.answer(
            f"Вы выбрали женское имя и фамилию, продолжаю процесс генерации...\n{response}",reply_markup=builder.as_markup())
    elif callback_query.data == "option_foreign_male":
        response = gen_foreign_male()
        builder = InlineKeyboardBuilder()
        builder.button(text="в избранное", callback_data=f"favorite_{response}",reply_markup = builder.as_markup())
        await callback_query.message.answer(
            f"Вы выбрали мужское имя и фамилию, продолжаю процесс генерации...\n{response}",reply_markup = builder.as_markup())
    elif callback_query.data == "option_foreign_female":
        response = gen_foreign_female()
        builder = InlineKeyboardBuilder()
        builder.button(text="в избранное", callback_data=f"favorite_{response}",reply_markup = builder.as_markup())
        await callback_query.message.answer(
            f"Вы выбрали женское имя и фамилию, продолжаю процесс генерации...\n{response}",reply_markup = builder.as_markup())
    elif callback_query.data == "option_fantasy_male":
        response = gen_fantasy_male()
        builder = InlineKeyboardBuilder()
        builder.button(text="в избранное", callback_data=f"favorite_{response}")
        await callback_query.message.answer(
            f"Вы выбрали мужское имя и фамилию, продолжаю процесс генерации...\n{response}",reply_markup = builder.as_markup())
    elif callback_query.data == "option_fantasy_female":
        response = gen_fantasy_female()
        builder = InlineKeyboardBuilder()
        builder.button(text="в избранное", callback_data=f"favorite_{response}")
        await callback_query.message.answer(
            f"Вы выбрали женское имя и фамилию, продолжаю процесс генерации...\n{response}",reply_markup = builder.as_markup())

    if callback_query.data == "option_russian":
        data[id]["type"] = "russian"
        await callback_query.message.answer("Вы выбрали русский тип имени и фамилии.")
    elif callback_query.data == "option_foreign":
        data[id]["type"] = "foreign"
        await callback_query.message.answer("Вы выбрали иностранный тип имени и фамилии.")
    elif callback_query.data == "option_fantasy":
        data[id]["type"] = "fantasy"
        await callback_query.message.answer("Вы выбрали фентезийный тип имени и фамилии.")

@dp.callback_query(lambda c:c.data.startswith("favorite"))
async def favorite_callback(callback_query: CallbackQuery):
    await callback_query.answer()
    id = callback_query.from_user.id
    _ , name = callback_query.data.split('_')
    name = name.strip()
    if name not in data[id]['favorite']:
        data[id]['favorite'].append(name)
    print(data[id]["favorite"])

    with open("data.json", "w") as dt:
        json.dump(data, dt)

@dp.message(Command(commands=['favorite']))
async def favorite_list(message: Message):
    id = message.from_user.id
    print(type(id))

    answer = ''
    for i in data[id]["favorite"][::-1]:
        answer += i +'\n'

    await message.answer(f"Ваш список избранных: \n{answer}")

@dp.message(Command(commands=['clean_favorite']))
async def favorite_list(message: Message):
    id = message.from_user.id
    data[id]["favorite"]=[]

    with open("data.json", "w") as dt:
        json.dump(data, dt)

    await message.answer("ОЧИСТКА ЕРЕСИ прошла успешно!")


@dp.message(Command(commands=['see']))
async def see(message: Message):
    id = message.from_user.id
    if id == 8133985440:
        await message.answer("Добро пожаловать, инквизитор.")
        answer = ''
        for i in data:
            answer += f'\nid пользователя: {i} \n'
            answer += f'имя пользователя: {data[i]["name"]} \n'
            answer += f'имя пользователя: {data[i]["username"]} \n'
            answer +='\n'
            for j in data[i]["favorite"][::-1]:
                answer += j + '\n'
        await message.answer(f"Ваш список избранных: \n{answer}")

@dp.message(Command(commands=['go_to_test']))
async def go_to_test (message: Message, command: CommandObject):
    id = message.from_user.id

    if id == 8133985440:
        await message.answer("Добро пожаловать, инквизитор.")
        if command.args:
            message_for_users = command.args
        print(command.args)
        for i in data:
            await error_check(i, message_for_users)


async def error_check(id, message_for_users):
    try:
        await bot.send_message(id, message_for_users)
    except:
        print(f"bot was blocked by the user {data[id]['name']}")
    else:
        print("message sent")


@dp.message()
async def echo(message: Message):
    id = message.from_user.id
    print(message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
