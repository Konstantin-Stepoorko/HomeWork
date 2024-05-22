# Реляционная База Данных: SQLite
import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('telemetry.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS rocket_space
(id_rs INTEGER PRIMARY KEY,
name_spacecraft TEXT,
link_start TEXT)
''')

# Вставка данных
cursor.execute("INSERT INTO rocket_space (name_spacecraft, link_start) VALUES ('Союз-ФГ', 'https://www.youtube.com/watch?v=UNlglX8IiFo')")
cursor.execute("INSERT INTO rocket_space (name_spacecraft, link_start) VALUES ('Атлантис', 'https://dewesoft.com/ru/blog/nasa-pcm-telemetry-processing-station')")
cursor.execute("INSERT INTO rocket_space (name_spacecraft, link_start) VALUES ('Ангара', 'https://www.youtube.com/watch?v=09lmZUp5RcE')")

# Запрос данных
cursor.execute("SELECT * FROM rocket_space")
print(cursor.fetchall())

# Закрытие соединения
conn.commit()
conn.close()
