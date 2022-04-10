import requests
from bs4 import BeautifulSoup as BS
from config import tg_bot_token_Airat, admins, tg_bot_token_Nail
import markups as nav
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import change_xlsx
import datetime
from readd_db import read_db, write_school, clear_db_users

bot = Bot(token=tg_bot_token_Airat)  # to_db
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    # add a person to the DB if he is not there
    # await bot.edit_message_reply_markup(chat_id=message.from_user.id, reply_markup=nav.defaultMenu)
    await bot.send_message(message.from_user.id, "Выберите район и школу, и я отправлю вам школьное меню на сегодня.",
                           reply_markup=nav.inlineMenu)


@dp.message_handler(commands=["support"])
async def support_team(message: types.Message):
    if int(message.from_user.id) not in admins:
        await bot.send_message(message.from_user.id, f"{message.from_user.id}", reply_markup=nav.inlineMinorMenu)
    else:
        await bot.send_message(message.from_user.id, "Че-то админское", reply_markup=nav.inlineMinorMenu)


@dp.message_handler()
async def get_menu(message: types.Message):
    try:

        if message.text == 'Получить меню' and True:
            # change when connecting db person-school
            # change when connecting the db with area-schools
            r = requests.get("https://edu.tatar.ru/n_chelny/lic-int79/food")
            soup = BS(r.content, 'html.parser')
            # name = 'https://edu.tatar.ru' + soup.find('div', id='school_data').find('a').get('href')
            # await message.reply(ad.print_menu(name))
            if datetime.date.today():  # in db
                change_xlsx.give_menu('https://edu.tatar.ru' + soup.find('div', id='school_data').find('a').get('href'))
                await bot.send_message(message.from_user.id, change_xlsx.print_menu('menu.xlsx'))
            else:
                await bot.send_message(message.from_user.id, "Пожалуйста, подождите")
                # await bot.send_message(message.from_user.id, f"{give_menu()}")
                # load menu into db
        elif message.text == 'Изменить школу':
            clear_db_users(message.from_user.id)
            await bot.send_message(message.from_user.id, "Вы перешли в главное меню", reply_markup=nav.inlineMenu)
        else:
            # change when connecting db person-school
            await bot.send_message(message.from_user.id, "Я вас не понимаю", reply_markup=nav.minorMenu)
    except:
        await message.reply(f"Произошла какая-то ошибка.")


@dp.callback_query_handler(text="btn_n_chelny")
async def n_chelny(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите школу", reply_markup=nav.inlineMinorMenu)


@dp.callback_query_handler(text="btn_lic_int79")
async def lic_int79(message: types.Message):
    write_school(message.from_user.id, "Лицей-интернат №79")
    await bot.send_message(message.from_user.id, "Спасибо, теперь, если ваша школа опубликовала"
                                                 " меню на сайте edu.tatar, то вы можете его получить.",
                           reply_markup=nav.minorMenu)


@dp.callback_query_handler(text="btn_sch78")
async def sch78(message: types.Message):
    write_school(message.from_user.id, "Лицей №78")
    await bot.send_message(message.from_user.id, "Спасибо, теперь, если ваша школа опубликовала"
                                                 " меню на сайте edu.tatar, то вы можете его получить.",
                           reply_markup=nav.minorMenu)


@dp.callback_query_handler(text="btn_gym26")
async def gym26(message: types.Message):
    write_school(message.from_user.id, "Гимназия №26")
    await bot.send_message(message.from_user.id, "Спасибо, теперь, если ваша школа опубликовала"
                                                 " меню на сайте edu.tatar, то вы можете его получить.",
                           reply_markup=nav.minorMenu)


if __name__ == '__main__':
    executor.start_polling(dp) # ее моее
