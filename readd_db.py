import _sqlite3


def read_db(school_name, area_name):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    information = cur.execute(
        f"SELECT schools, data_obnovlenia, menu, papka FROM {area_name}").fetchall()
    cur.close()
    for elem in information:
        sch_full_name, data_obnovlenia, menu, papka = elem
        if sch_full_name == school_name:
            information_1 = elem
    return information_1


def write_school(id_users, school_name):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO users (users_id, users_school) values(?, ?);""", (id_users, school_name))
    con.commit()
    cur.close()


def clear_db_users(id_users):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    cur.execute("""DELETE FROM users WHERE users_id = ? ;""", (id_users,))
    con.commit()
    cur.close()


def get_school(id_users):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    school_name, *k = cur.execute(
        f"SELECT users_school FROM users WHERE users_id = {id_users}").fetchall()[0]
    cur.close()
    return school_name


def check_users(id_users):
    Users_in = False
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    inf = cur.execute(
        f"SELECT users_id FROM users").fetchall()
    cur.close()
    for elem in inf:
        id, = elem
        if str(id_users).strip() == str(id).strip():
            Users_in = True

    return Users_in


def write_menu_date_update(school_name, menu, date_update):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    cur.execute("""UPDATE n_chelny SET menu = ? WHERE schools = ?""", (menu, school_name))
    cur.execute("""UPDATE n_chelny SET data_obnovlenia = ? WHERE schools = ?""", (date_update, school_name))
    con.commit()
    cur.close()
