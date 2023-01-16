from config import ADMINS, bot
from aiogram import types, Dispatcher

async def pin(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        else:
            await bot.send_message(message.chat.id, 'отметьте для закрепления!')
    else:
        await message.reply('Только для админов!')




def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')