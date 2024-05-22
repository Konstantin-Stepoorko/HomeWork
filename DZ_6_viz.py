# Визуализация данных из таблицы телеметрии БД
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
import math

def int_sec(str):
  sec=0
  j=0
  for i in reversed(list(str.split(':'))):
    sec += int(i)*60**j
    j += 1
  return(sec)

try:

    сonn = sqlite3.connect('telemetry.db')
    print("Подключено к telemetry.db")

    sql_q = """SELECT COUNT(*) FROM telemetry WHERE overload>0;"""
    curs = сonn.cursor()
    curs.execute(sql_q)
    print("\nДанные таблицы telemetry:")
    print(curs.fetchone()[0])

    sql_q = """SELECT timer, height, distance, speed FROM telemetry;"""
    curs.execute(sql_q)
    rows = curs.fetchall()

    y=len(rows)
    print(y)

    X_col = np.empty(y)
    y_col = np.empty(y)
    y_col1 = np.empty(y)
    y_col2 = np.empty(y)
    y_col3 = np.empty(y)

    i = 0

    fig, axs = plt.subplots(figsize=(16,4), ncols=3)  # заготовка поля для графиков
    for row in rows:
      y_col1[i] = row[1]
      y_col2[i] = row[2]
      y_col3[i] = row[3]
      X_col[i] = int_sec(row[0])
      y_col[i] = (row[1]**2 + row[2]**2)**0.5
      i += 1

    # ОТРИСОВКА ГРАФИКОВ
    axs[0].plot(X_col, y_col1, label='График 1')
    axs[1].plot(X_col, y_col2, label='График 2')
    axs[2].plot(X_col, y_col3, label='График 3')

    axs[0].legend()

    axs[0].set_title('Зависимость высоты от времени')
    axs[1].set_title('Зависимость дальности от времени')
    axs[2].set_title('Зависимость скорости от времени')

    # ОТРИСОВКА ГРАФИКОВ

    plt.figure(figsize=(20,6))
    sns.lineplot(x=X_col,y=y_col)
    sns.set_style('darkgrid')
    plt.title('Телеметрия старта КА')
    plt.xticks(rotation=90)
    plt.show

    # Создаем график распределения
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(y_col1, bins=50, kde=True, color="skyblue")
    plt.title('График распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.show()

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(y_col2, bins=50, kde=True, color="skyblue")
    plt.title('График распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.show()

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(y_col3, bins=50, kde=True, color="skyblue")
    plt.title('График распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.show()

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(y_col, bins=50, kde=True, color="skyblue")
    plt.title('График распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.show()

except sqlite3.Error as error:
    print("Не удалось выполнить вышеуказанный запрос", error)

finally:

    if сonn:
        # Закрываем соединение, если оно было открыто
        сonn.close()

        print("\nСоединение закрыто")
