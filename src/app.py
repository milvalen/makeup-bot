import logging
import asyncio
import os

from aiogram import Bot, Dispatcher

from src.handlers import questions

with open(f'{os.getcwd()}/src/env/token.txt') as f:
    BOT_TOKEN = f.read().strip()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():

    dp.include_routers(questions.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
