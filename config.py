from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN = config("TOKEN")
ADMINS = (337453696,)

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)