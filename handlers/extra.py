from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice


async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    elif message.text.lower().startswith('game'):
        if message.from_user.id in ADMINS:
            games = ['⚽️', '🏀', '🎳', '🎲', '🎯', '🎰']
            rand = choice(games)
            await bot.send_dice(message.chat.id, emoji=rand)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
