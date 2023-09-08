############# CREATE ALL ###############

import sqlite3

db = sqlite3.connect("database.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS income_history (
    category TEXT,
    income BIGINT,
    date TEXT
)""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS expense_history (
            category TEXT,
            expense BIGINT,
            date TEXT
        )""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS balance (
            balance BIGINT
        )""")
db.commit()

############ DELETE ALL ################

# import sqlite3
#
# # Устанавливаем соединение с базой данных
# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()
#
# # Получаем список всех таблиц в базе данных
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
#
# # Удаляем каждую таблицу
# for table in tables:
#     table_name = table[0]
#     cursor.execute(f"DROP TABLE {table_name}")
#
# # Сохраняем изменения и закрываем соединение
# conn.commit()
# conn.close()
