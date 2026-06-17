import os
import logging
import httpx
from telegram.ext import Application
from fastapi import FastAPI, Request
import uvicorn

BOT_TOKEN = os.getenv("BOT_TOKEN")
# ВАШ URL (без слеша в конце)
WEBHOOK_URL = "https://vasvis-sheserch.hf.space"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
application = Application.builder().token(BOT_TOKEN).build()

@app.on_event("startup")
async def startup():
    # Прокси для установки вебхука
    proxy = "http://185.162.229.204:80" 
    
    logger.info("Попытка установки вебхука через прокси...")
    
    # Регистрация вебхука через прокси-сервер
    async with httpx.AsyncClient(proxies=proxy, timeout=30.0) as client:
        # Прямой вызов API Telegram
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}/telegram"
        response = await client.get(url)
        if response.status_code == 200:
            logger.info("Webhook успешно установлен!")
        else:
            logger.error(f"Ошибка установки: {response.text}")

    await application.initialize()
    await application.start()

@app.post("/telegram")
async def telegram_webhook(request: Request):
    update_data = await request.json()
    # Обработка входящего сообщения
    await application.update_queue.put(update_data)
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)