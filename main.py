import config
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from random import randint


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.tgtoken)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\n Это бот с анекдотами \n/get")

@dp.message_handler(commands=['get'])
async def send_anecdot(message: types.Message):
    await message.reply(config.anecdot[randint(0, len(config.anecdot)-1)])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)