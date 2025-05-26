import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_NAME")

bot = Bot(token=TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! Это SkyFreeLanc Bot.\n"
        "Отправь /postjob <текст вакансии>, чтобы опубликовать её в канале."
    )

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/start — приветствие\n"
        "/help — помощь\n"
        "/postjob <текст> — опубликовать вакансию в канале"
    )

def post_job(update: Update, context: CallbackContext):
    job_text = ' '.join(context.args)
    if not job_text:
        update.message.reply_text("Ошибка: нужно написать текст вакансии после команды.")
        return

    try:
        bot.send_message(chat_id=CHANNEL, text=job_text)
        update.message.reply_text("Вакансия опубликована!")
    except Exception as e:
        update.message.reply_text(f"Ошибка при публикации: {e}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("postjob", post_job))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
