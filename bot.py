from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
# Загрузка переменных окружения
from dotenv import load_dotenv
import os
import random

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()  # Для версии 3.x бот не передается в конструктор

# Список предсказаний
predictions = [
    "Сегодня вас ждёт успех!",
    "Удача на вашей стороне",
    "Время для новых начинаний",
    "Ждите приятного сюрприза"
]


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        f"Мое предсказание: {random.choice(predictions)}"
    )