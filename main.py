

from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("✅ Bot funcionando com sucesso!")

def main():
    # Substitua este token pelo seu, se for diferente
    updater = Updater("6670101561:AAH5n3rXZmxp6AKXoYlhNv-yA4iOE5QoXlI", use_context=True)
    dp = updater.dispatcher

    # Comando /start
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()