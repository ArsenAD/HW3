from aiogram import Bot, Dispatcher
from decouple import config



TOKEN = config("TOKEN")
ADMINS = (337453696,)

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)