from config import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def quiz_2(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT2', callback_data='button_call_2')
    murkup.add(button_call_2)
    question = "какой напиток содержит больше алкоголя"
    answers = [
        'балтика 9',
        'швепс',
        'джин',
        'ягуар',
        'абсент',
        'водка'
    ]
    await bot.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation='ezz',
        open_period=20,
        reply_markup=murkup
    )


async def quiz_3(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('finish', callback_data='button_call_3')
    murkup.add(button_call_3)
    question = "Настоящая фамилия Сталина"
    answers = [
        'Иосиф',
        'Джигурда',
        'Путин',
        'Джугашвили',
        'Шпиливили',
        'Мартиросян'
    ]
    await bot.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='ezz',
        open_period=20,
        reply_markup=murkup
    )



async def quiz_4(message: types.Message):
    pass

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
    dp.register_callback_query_handler(quiz_3, text='button_call_2')
    dp.register_callback_query_handler(quiz_4, text='button_call_3')

