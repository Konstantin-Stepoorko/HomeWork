import sqlite3 as sq

# Подключение к SQLite базе данных (или создание, если не существует)
conn = sq.connect('telemetry.db')
cursor = conn.cursor()

# Создание таблицы "stage_launch" "'этапы запуска'"
cursor.execute('''
  CREATE TABLE IF NOT EXISTS stage_launch
  (id_sl INTEGER PRIMARY KEY,
  name_stage TEXT NOT NULL,
  name TEXT)
''')

# Вставка разнообразных данных
users_data = [
    ( '1-й этап', 'разгон первой ступени', ),
    ( '2-й этап', 'разгон второй ступени', ),
    ( '3-й этап', 'разгон третей ступени', ),
    ( '4-й этап', 'невесомость', )
]

cursor.executemany("INSERT INTO stage_launch (name_stage, name) VALUES (?, ?)", users_data)

# Запрос данных
cursor.execute("SELECT * FROM stage_launch")
names = cursor.fetchall()
for name in names:
    print(name)

# Создание таблицы "stage_launch_rocket" "'этапы запуска конкретного КА'"
cursor.execute('''
  CREATE TABLE IF NOT EXISTS stage_launch_rocket
  (
    id_sl_r INTEGER PRIMARY KEY,
    id_rs INTEGER NOT NULL,
    id_sl INTEGER NOT NULL,
    start_time REAL,
    end_time REAL,
    FOREIGN KEY (id_rs) REFERENCES rocket_space (id_rs),
    FOREIGN KEY (id_sl) REFERENCES stage_launch (id_sl)
  )
''')

# Вставка разнообразных данных
users_data = [
    (1, 1, 0.0, 117.80, ),
    (1, 2, 117.81, 287.30, ),
    (1, 3, 287.31, 528.26, ),
    (1, 4, 528.27, 99999, )
]

cursor.executemany("INSERT INTO stage_launch_rocket (id_rs, id_sl, start_time, end_time) VALUES (?, ?, ?, ?)", users_data)

# Запрос данных
cursor.execute("SELECT * FROM stage_launch_rocket")
names = cursor.fetchall()
for name in names:
    print(name)

# Закрытие соединения и сохранение изменений
conn.commit()
conn.close()
