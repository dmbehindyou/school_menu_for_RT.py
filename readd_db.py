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
