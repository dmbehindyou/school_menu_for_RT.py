import os
import datetime
import _sqlite3
import requests
import xlrd
import shutil


#  install pyexcel-xls, pyexcel-xlsx
def read_db(nomer):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    # def Connect_coursore():
    information = cur.execute(
        "SELECT schools, get_search FROM n_chelny").fetchall()[nomer - 1]
    cur.close()
    return information


def create_dict(area_name):
    dict_schools = {}
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    information = cur.execute(
        f"SELECT id, schools, get_search FROM {area_name}").fetchall()
    cur.close()
    for elem in information:
        id, schools, get_search = elem
        dict_schools[schools] = id
    return dict_schools


def print_menu(book):
    book = xlrd.open_workbook(book)
    sheet = book.sheet_by_index(0)
    priem_pishi, menu = [], ''
    ne_school = True
    max_i = 0
    try:
        for i in range(4, 25):
            if sheet.cell_value(i - 1, 0) == "Школа":
                ne_school = False
            if ne_school:
                if sheet.cell_value(i - 1, 0) != 42:
                    priem_pishi.append(sheet.cell_value(i - 1, 0))
            max_i = i
    except IndexError:
        pass
    i = 3
    for elem in priem_pishi:
        chto_dayt = ''
        if elem != priem_pishi[-1]:
            i += 1
            while sheet.cell_value(i, 0) != priem_pishi[priem_pishi.index(elem) + 1]:
                chto_dayt += f'{sheet.cell_value(i - 1, 3)} ({int(sheet.cell_value(i - 1, 4))} гр.)\n'
                i += 1
            chto_dayt += f'{sheet.cell_value(i - 1, 3)} ({int(sheet.cell_value(i - 1, 4))} гр.)\n'

        else:
            try:
                if i < 4:
                    i += 1
                while sheet.cell_value(i + 1, 3) != 42 and sheet.cell_value(i + 1, 0) != 'Школа':
                    chto_dayt += f'{sheet.cell_value(i, 3)} ({int(sheet.cell_value(i, 4))} гр.)\n'
                    i += 1
                chto_dayt += f'{sheet.cell_value(i, 3)} ({int(sheet.cell_value(i, 4))} гр.)\n'
            except IndexError:
                chto_dayt += f'{sheet.cell_value(i, 3)} ({int(sheet.cell_value(i, 4))} гр.)\n'
        menu += f'{elem}:\n{chto_dayt}\n'
    return menu


def give_menu(url=''):
    try:
        response = requests.get(url=url)
        with open("menu.xlsx", 'wb') as f:
            f.write(response.content)
    except:
        return 'Ё-моё, у нас проблемы'


# area_name = 'n_chelny'  # input()
# school_name = 'МБОУ "Лицей-интернат №79"'  # input()
# print(read_db(nomer)) ('МБОУ "Лицей-интернат №79"', 'lic-int79/food', 'A4', 'D3')
# sch_full_name, get = read_db(create_dict(area_name)[school_name])
# date = str(datetime.datetime.now().date())
# spisok_file = os.listdir()
# file_name = "2022-04-08-sm.xlsx"
# file_name = xlrd.open_workbook(file_name)
# print_menu(file_name)
