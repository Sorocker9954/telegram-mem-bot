from telegram import Bot
from telegram.ext import CommandHandler, Updater

def start(update, context):
    update.message.reply_text('Hello, this is your meme bot!')

def main():
    bot = Bot(token='7216283940:AAFB1h9Otl8NhC19ElPvpKmzCsVs8QMOsos')
    updater = Updater(token='7216283940:AAFB1h9Otl8NhC19ElPvpKmzCsVs8QMOsos', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
