from aiogram.utils import executor
from config import dp, bot, ADMINS
import logging
from handlers import client, callback, extra, admin, FsmAdminmentor


async def on_startup(_):
    await bot.send_message(chat_id=ADMINS[0],
                           text='Bot started!')


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handler_admin(dp)
FsmAdminmentor.register_handlers_mentors(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
