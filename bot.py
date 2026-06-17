import os
import sys
import logging
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
    print("КРИТИЧЕСКАЯ ОШИБКА: Переменная среды BOT_TOKEN не найдена!")
    sys.exit(1)
else:
    # Удаляем лишние пробелы или переносы строк, которые могли попасть при копировании в Railway
    BOT_TOKEN = BOT_TOKEN.strip()
    print(f"Токен загружен (длина: {len(BOT_TOKEN)})")
