import sqlite3


class Database:
    def __init__(self):
        self.connection=sqlite3.connect("evos.db")
        self.cursor=self.connection.cursor()

    def create_user_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY,
            first_name varchar(55)not null,
            last_name varchar(55),
            age integer,
            address varchar(255),
            telegram_id integer not null unique
            )
        """)

database=Database()
database.create_user_table()