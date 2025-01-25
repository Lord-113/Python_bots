import linecache, random
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

def gen_male():
    return linecache.getline("names_m.txt", random.randint(1, 90)).strip() + ' ' + \
        linecache.getline("surnames.txt", random.randint(1, 14650))


def gen_female():
    name = linecache.getline("names_f.txt", random.randint(1, 68)).strip()
    surname = linecache.getline("surnames.txt", random.randint(1, 14650)).strip()
    if surname[-1] == 'в' or surname[-1] == 'н':
        surname += 'а'
    elif surname[-2:] == 'ий':
        surname = surname[:-2] + 'ая'

    return name + ' ' + surname
