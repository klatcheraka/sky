from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")

print(f"Токен загружен: {repr(TOKEN)}")
print(f"Канал: {repr(CHANNEL)}")

if not TOKEN or ":" not in TOKEN:
    raise ValueError("Токен не найден или неверного формата!")

bot = Bot(token=TOKEN)

def start(update: Update, context):
    update.message.reply_text("Привет! Я SkyFreeLanc бот.")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
print("Бот запущен...")
updater.idle()