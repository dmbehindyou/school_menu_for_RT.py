import requests
from bs4 import BeautifulSoup as BS
from config import tg_bot_token_Airat, admins, tg_bot_token_Nail
import markups as nav
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import change_xlsx
import datetime
from readd_db import read_db, write_school, clear_db_users, get_school, check_users, write_menu_date_update

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
        if message.text == 'Получить меню' and check_users(message.from_user.id):
            sch_full_name, data_update, menu, link = read_db(get_school(message.from_user.id), 'n_chelny')
            if datetime.date.today() == data_update:
                await bot.send_message(message.from_user.id, menu)
            else:
                try:
                    await bot.send_message(message.from_user.id, "Пожалуйста, подождите")
                    change_xlsx.give_menu(link + str(datetime.date.today()) + '-sm.xlsx')
                    print_menu('menu.xlsx')
                except:
                    await bot.send_message(message.from_user.id, "Вашего меню ещё нет...")
        elif message.text == 'Получить меню':
            await bot.send_message(message.from_user.id, "Пожалуйста, выберите школу", reply_markup=nav.inlineMenu)
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
    executor.start_polling(dp)
