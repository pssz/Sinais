from telegram import Update, Bot, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext

# Token do seu bot do Telegram
TOKEN = "6670101561:AAH5n3rXZmxp6AKXoYlhNv-yA4iOE5QoXlI"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Bot funcionando no Render ✅")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
