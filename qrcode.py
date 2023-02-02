from aiogram import types, Dispatcher
import pyqrcode as pq
from config import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext



class Code(StatesGroup):
    qr_mess = State()
    qr_create = State()


async def qr_code_gen(message: types.Message):
    await Code.qr_mess.set()
    await message.reply('отправьте ссылку для создания QR кода для выбранного сайта!')
    if message.text is not None:
       await Code.next()




async def qr_based(message: types.Message, state: FSMContext):
        await message.answer('Ваша ссыока принята! идет генерация QR кода!')
        qr_code = pq.create(message.text)
        qr_code.png('code.png', scale=6)
        with open('code.png', 'rb') as photo:
            await bot.send_photo(message.chat.id, photo)
            await bot.send_message(message.chat.id, 'Ваш QR код готов!')
            await state.finish()



def register_handlers_qr(dp: Dispatcher):
    dp.register_message_handler(qr_code_gen, commands=['qr'])
    dp.register_message_handler(qr_based, state=Code.qr_create)
