import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer("Ok")


async def go_to_git():
    for id in chat_id:
        await bot.send_message(id, "Надо учиться!")


async def go_to_gym():
    for id in chat_id:
        await bot.send_message(id, "пора тренить чемпион!")


async def scheduler():
    aioschedule.every().thursday.at('17:30').do(go_to_git)
    aioschedule.every().thursday.at('06:30').do(go_to_gim())
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)