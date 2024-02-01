from aiogram import Bot, Dispatcher, F
from asyncio import run

import callback_functions
import funksiyalar

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(5165396993, "Bot ishga tushdi! ✅")
async def shutdown_answer(bot: Bot):
    await bot.send_message(5165396993, "Bot ishdan to'xtadi! ❗")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(funksiyalar.open_calc_answer)

    dp.callback_query.register(callback_functions.callback_answer)

    bot = Bot("6923568104:AAG5CQOmPU0_cG-Ym3dwdGNC5ZFjRcYB9cY")
    await dp.start_polling(bot, polling_timeout=1)

run(start())