import os
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

bot = telegram.Bot(token=TOKEN)

def start(update, context):
    context.bot.send_message(chat_id=CHAT_ID, text="✅ Bot iniciado com sucesso!")

def alerta(update, context):
    mensagem = ' '.join(context.args)
    context.bot.send_message(chat_id=CHAT_ID, text=f"📢 Alerta de sinal: {mensagem}")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('alerta', alerta))

updater.start_polling()
