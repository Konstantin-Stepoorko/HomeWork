# Чтение всех таблиц, созданных в БД
import sqlite3

try:

    сonn = sqlite3.connect('telemetry.db')

    # Если соединение установлено
    # программа выведет сообщение "Подключено к telemetry.db"
    # иначе выведет show errors
    print("Подключено к telemetry.db")

    # Получение всех таблиц из sqlite_master
    sql_q = """SELECT name FROM sqlite_master WHERE type='table';"""

    # Создание курсора
    curs = сonn.cursor()

    # выполнение sql запроса
    curs.execute(sql_q)
    print("\nСписок таблиц:")

    tables = curs.fetchall()

    # выводим список всех таблиц
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}\n")
        sql_q = f"SELECT * from {table_name}"
        curs = сonn.execute(sql_q)
        names = list(map(lambda x: x[0], curs.description))
        for name in names:
            print(f"column: {name}")

except sqlite3.Error as error:
    print("Не удалось выполнить вышеуказанный запрос", error)

finally:

    # Inside Finally Block, If connection is
    # open, we need to close it
    if сonn:
        # Закрываем соединение, если оно было открыто
        сonn.close()

        print("\nСоединение закрыто")
