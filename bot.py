import requests
from bs4 import BeautifulSoup as BS
from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет, напиши название школы и района и я отправлю тебе меню на сегодня")


@dp.message_handler()
async def get_menu(message: types.Message):
    try:
        if message.text == 'Лицей-интернат 79':
            r = requests.get("https://edu.tatar.ru/n_chelny/lic-int79/food")
            soup = BS(r.content, 'html.parser')
            name = soup.find('div', id='school_data').find('a').get('href')
            await message.reply('https://edu.tatar.ru' + name)
    except:
        await message.reply("Я вас не понимаю, попробуйте ещё раз.")


if __name__ == '__main__':
    executor.start_polling(dp)
