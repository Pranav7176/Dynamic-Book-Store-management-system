

import pysqlite3
def exee(command):
    cur.execute(command)
    con.commit()

con=pysqlite3.connect("bookStore.db")
cur=con.cursor()
if __name__ == '__main__':
    # exee("""CREATE TABLE IF NOT EXISTS Books(ID INTEGER PRIMARY KEY, Title TEXT NOT NULL)""")
    # exee("""CREATE TABLE IF NOT EXISTS Books(ID INTEGER PRIMARY KEY, Title TEXT NOT NULL)""")

    # exee("""INSERT INTO Books(TITLE) VALUES('c++'), ('python'), ('java'), ('c'), ('CLRS'), ('R.D.Sharma'), ('OOPS IN PYTHON'), ('OOPS IN C++'), ('OOPS IN JAVA')""")

    # exee("""UPDATE Books SET TITLE="JAVA" WHERE ID=2""")

    # exee("""SELECT * FROM Books WHERE ID=1""")
    # print(cur.fetchall())
    cur.execute("""DELETE FROM Books WHERE TITLE="python" """)
    cur.execute("""SELECT * FROM Books where TITLE=?""", ("python",))
    result = cur.fetchall()
    if result:
        print(result)
    else:
        print("No book found with the given title.")
    pass