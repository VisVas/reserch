import os
import sys
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Загрузка токена
BOT_TOKEN ="7956580714:AAEVe-I_oPBLfoSuCfc90oC0HLGA0O6AUWY"

if not BOT_TOKEN:
    logger.error("КРИТИЧЕСКАЯ ОШИБКА: Переменная BOT_TOKEN не найдена!")
    sys.exit(1)

BOT_TOKEN = BOT_TOKEN.strip()
logger.info(f"Токен загружен (длина: {len(BOT_TOKEN)})")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ответ на команду /start"""
    user_id = update.effective_user.id
    logger.info(f"Получена команда /start от пользователя {user_id}")
    try:
        await update.message.reply_text("Привет! Я работаю на Railway, и у меня всё отлично!")
        logger.info(f"Ответ успешно отправлен пользователю {user_id}")
    except Exception as e:
        logger.error(f"Ошибка при отправке ответа: {e}")

async def main():
    """Главная функция запуска бота"""
    try:
        # Инициализация бота
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Принудительное удаление вебхука, если он был установлен ранее
        await application.bot.delete_webhook()
        logger.info("Старые вебхуки удалены, работаем через Polling")
        
        # Добавляем обработчик
        application.add_handler(CommandHandler("start", start))
        
        # Запуск бота
        logger.info("Запуск бота...")
        await application.initialize()
        await application.start()
        await application.updater.start_polling()
        
        logger.info("Бот успешно запущен и слушает сообщения!")
        
        # Держим процесс активным
        await asyncio.Event().wait()
        
    except Exception as e:
        logger.error(f"Критическая ошибка при работе бота: {e}")

if __name__ == "__main__":
    asyncio.run(main())
