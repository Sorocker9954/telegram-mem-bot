from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, this is your meme bot!')

# Основная функция, которая запускает бота
def main():
    # Указываем токен и создаём приложение (бота)
    application = Application.builder().token('7216283940:AAFB1h9Otl8NhC19ElPvpKmzCsVs8QMOsos').build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
