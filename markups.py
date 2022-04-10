from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btnChangeSchool = KeyboardButton('Изменить школу')
btnGetMenu = KeyboardButton('Получить меню')
btnSupport = KeyboardButton('/support')
minorMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnChangeSchool, btnGetMenu, btnSupport)


defaultMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSupport)


btn_n_chelny = InlineKeyboardButton(text="г. Набережные Челны", callback_data="btn_n_chelny")
inlineMenu = InlineKeyboardMarkup(row_width=2).insert(btn_n_chelny)

btn_lic_int79 = InlineKeyboardButton(text="Лицей-интернат №79", callback_data="btn_lic_int79")
btn_sch78 = InlineKeyboardButton(text="Лицей №78", callback_data="btn_sch78")
btn_gym26 = InlineKeyboardButton(text="Гимназия №26", callback_data="btn_gym26")
inlineMinorMenu = InlineKeyboardMarkup(row_width=2).add(btn_lic_int79, btn_sch78, btn_gym26)
