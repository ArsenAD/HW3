from config import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from parser.movie import parser



# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,  f'Привет {message.from_user.first_name}!')

    await message.answer('Ответ на ваше сообщение')

    await message.reply('коммент на ваше сообщение')

# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    murkup.add(button_call_1)
    question = "что продается в магазине Hobby Games"
    answers = [
        'Конц товары',
        'Продукты питания',
        'Женское белье',
        'Настольные игры',
        'Сахарную вату'
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

async def mem1(message: types.Message):
    photo = open('media/mem4ik.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    photo.close()

async def get_movie(message: types.Message):
    movie = parser()
    for i in movie:
        await message.answer(
            f"{i['link']}\n\n"
            f"{i['title']}\n"
            f"{i['date']}\n"
            f"{i['gener']}\n"
            f"{i['views']}\n"
        )



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem1, commands=['mem'])
    dp.register_message_handler(get_movie, commands=['movie'])
