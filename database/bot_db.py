import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('База данных подключена!')

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(t_id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "mentorsname VARCHAR (255), "
               "direction  VARCHAR (255), "
               "age INTEGER, "
               "mentors_group TEXT)")
    db.commit()

sql_create()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors (t_id, mentorsname, direction, age, mentors_group) VALUES"
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    await bot.send_message(
        message.from_user.id,
        text=f"ID: {random_user[1]},\nDirection: {random_user[3]},\nAge:{random_user[4]} "
                f"\n\n{random_user[2]}"
    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()

