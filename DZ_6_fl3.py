# Загрузка таблицы из файла .csv, со значениями разделенными ";"
# функции доступны для импортирования

def login(dbfile):        # устанавливает соединение с БД "dbfile" и устанавливает курсор
  import sqlite3 as sql
  from sqlite3 import Error

  conn = None
  curs = None

  try:
    conn = sql.connect(dbfile)          # создать или открыть файл БД
    print("Connection to SQLite DB successful")
  except Error as e:
    print(f"The error '{e}' occurred")
    return conn, curs

  curs = conn.cursor()

  return conn, curs     # возвращает connector к БД и курсор

# выполням запрос к БД
def exec_q(conn, curs, query):
  import sqlite3 as sql
  from sqlite3 import Error
  try:
    curs.execute(query)
    print("Query executed successfully")
  except Error as e:            # except sqlite3.DatabaseError as e:
    print(f"The error '{e}' occurred")
  else:
    conn.commit()

# Работа с файлом
def read_f(r_file, curs):
  import csv
  import sqlite3 as sql
  from sqlite3 import Error

  with open(r_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ';')
    to_db = [(i['time'], i['height'], i['distance'], i['speed'], i['overload']) for i in reader]

  curs.executemany("INSERT INTO telemetry (timer,height,distance,speed,overload) VALUES (?, ?, ?, ?, ?);", to_db)

  print(type(to_db), to_db[0:3])

  print ( 'Прочитано: ', len(to_db), 'записей')

  # Cохранение изменений
  conn.commit()
  return len(to_db)

if __name__ == '__main__':

  conn, curs = login("telemetry.db")

  create_table = """
    CREATE TABLE IF NOT EXISTS telemetry(
      timer TEXT NOT NULL,
      height INTEGER,
      distance INTEGER,
      speed REAL,
      overload REAL)
  """
  exec_q(conn, curs, create_table)

  to_db = read_f('tel-01_05.csv', curs)

  # Закрытие соединения
  conn.close()
