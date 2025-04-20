from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Скинь мем, и я его отправлю на модерацию.')

# Функция для обработки сообщений с мемами (картинками)
async def handle_meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Проверяем, есть ли фото в сообщении
    if update.message.photo:
        photo_file = update.message.photo[-1].file_id  # Получаем файл с последним размером фото
        await update.message.reply_text(f'Мем получен! ID фото: {photo_file}')
        # Можем также добавить код, чтобы мем отправился в канал
        # await context.bot.send_photo(chat_id='@your_channel_id', photo=photo_file)
    elif update.message.text:
        await update.message.reply_text('Получен текст! Но только фото мемы обрабатываются.')

# Основная функция
def main():
    # Указываем токен и создаём приложение
    application = Application.builder().token('7216283940:AAFB1h9Otl8NhC19ElPvpKmzCsVs8QMOsos').build()

    # Регистрируем обработчики команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_meme))  # Для фото
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_meme))  # Для текста (опционально)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
