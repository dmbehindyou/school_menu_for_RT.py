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
