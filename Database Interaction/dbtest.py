#!usr/bin/python3


import sqlite3


def Main():
    try:
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        # Executing many commands as a single script
        cur.executescript("""
            DROP TABLE IF EXISTS Pets;
			CREATE TABLE Pets(Id INT, Name TEXT, Price INT);
			INSERT INTO Pets VALUES(1, 'Cat', 400);
			INSERT INTO Pets VALUES(2, 'Dog', 600);
            """)

        pets = ((3, "rabbit", 500),
                (4, "bird", 300),
                (5, "goat", 700)
                )
        cur.executemany("insert into Pets values(?, ?, ?)", pets)
        # Executing commands seperately
        # cur.execute("create table Pets(id Int, Name TEXT, Price INT)")
        # cur.execute("insert into Pets values(1, 'cat', 400)")
        # cur.execute("insert into Pets values(2, 'dog', 600)")
        # cur.execute("insert into Pets values(3, 'rabbit', 500)")
        # cur.execute("insert into Pets values(4, 'bird', 300)")

        con.commit()
        cur.execute("select * from Pets")
        data = cur.fetchall()
        for row in data:
            print(row)

    except sqlite3.Error:
        if con:
            print("Error! Rolling back!!")
            con.rollback()
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    Main()
