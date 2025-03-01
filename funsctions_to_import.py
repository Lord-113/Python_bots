import linecache, random
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


def gen_russ_male():
    return linecache.getline("names_russ_m.txt", random.randint(1, 90)).strip() + ' ' + \
        linecache.getline("surnames_russ.txt", random.randint(1, 14650))


def gen_russ_female():
    name = linecache.getline("names_russ_f.txt", random.randint(1, 68)).strip()
    surname = linecache.getline("surnames_russ.txt", random.randint(1, 14650)).strip()
    if surname[-1] == 'в' or surname[-1] == 'н':
        surname += 'а'
    elif surname[-2:] == 'ий' or surname[-2:] == 'ый' :
        surname = surname[:-2] + 'ая'

    return name + ' ' + surname


def gen_foreign_male():
    return linecache.getline("names_foreign_m.txt", random.randint(1, 195)).strip() + ' ' + \
        linecache.getline("surnames_foreign.txt", random.randint(1, 199))

def gen_foreign_female():
    return linecache.getline("names_foreign_f.txt", random.randint(1, 177)).strip() + ' ' + \
        linecache.getline("surnames_foreign.txt", random.randint(1, 199))

def gen_fantasy_male():
    return linecache.getline("names_fantasy_m.txt", random.randint(1, 242)).strip() + ' ' + \
        linecache.getline("surnames_fantasy.txt", random.randint(1, 231))

def gen_fantasy_female():
    return linecache.getline("names_fantasy_f.txt", random.randint(1, 175)).strip() + ' ' + \
        linecache.getline("surnames_fantasy.txt", random.randint(1, 231))
