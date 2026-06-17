import os
import sys

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("КРИТИЧЕСКАЯ ОШИБКА: Переменная среды BOT_TOKEN не найдена!")
    sys.exit(1)
else:
    # Удаляем лишние пробелы или переносы строк, которые могли попасть при копировании в Railway
    BOT_TOKEN = BOT_TOKEN.strip()
    print(f"Токен загружен (длина: {len(BOT_TOKEN)})")
