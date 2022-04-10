import _sqlite3

def write_school(id_users, school_name):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO users (id, schools) values(?, ?);""", (id_users, school_name))
    cur.close()

def clear_db_users(id_users):
    con = _sqlite3.connect('eaten_RT.db')
    cur = con.cursor()
    cur.execute("""DELETE FROM users WHERE id = ? ;""", (id_users))
    cur.close()