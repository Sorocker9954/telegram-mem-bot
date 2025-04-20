from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Список для хранения мемов в ожидании
memes_to_moderate = []

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Скинь мем, и я его отправлю на модерацию.')

# Функция для обработки сообщений с мемами (картинками)
async def handle_meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Проверяем, есть ли фото в сообщении
    if update.message.photo:
        photo_file = update.message.photo[-1].file_id  # Получаем файл с последним размером фото
        memes_to_moderate.append(photo_file)  # Сохраняем мем в список для модерации
        await update.message.reply_text(f'Мем получен! Он на модерации.')

# Функция для публикации мемов в канал (после модерации)
async def publish_meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if memes_to_moderate:
        meme = memes_to_moderate.pop(0)  # Берем следующий мем для публикации
        await context.bot.send_photo(chat_id='@lyagushkinilapki', photo=meme)
        await update.message.reply_text('Мем опубликован в канал!')
    else:
        await update.message.reply_text('Нет мемов на модерации.')

# Команда для публикации мемов (только для тебя, как админа)
async def admin_publish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Проверяем, что пользователь админ (например, по ID)
    if update.message.from_user.id == 909526370:  # Заменить на твой ID
        await publish_meme(update, context)
    else:
        await update.message.reply_text('У вас нет прав для публикации мемов.')

# Основная функция
def main():
    # Указываем токен и создаём приложение
    application = Application.builder().token('7216283940:AAFB1h9Otl8NhC19ElPvpKmzCsVs8QMOsos').build()

    # Регистрируем обработчики команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_meme))  # Для фото
    application.add_handler(CommandHandler("publish", admin_publish))  # Команда для админа

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
