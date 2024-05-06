from typing import ClassVar
from typing import Literal
# Домашняя работа 4 (Задания 1 - 12)
# Создание класса Автомобили

import random

class Car:

  count=0                     #Атрибут класса
  car_color='Black'           #Предустановленный атрибут класса
  engine_list = ['Бензиновый', 'Дизельный']

  def __init__(self, brand, year):
    self.brand = brand                     #название автомобиля
    self.year = year                       #год выпуска
    self.__engine_type = 'Дизельный'       #тип двигателя приватный атрибут

    Car.count += 1

  def start_engine(self, key=False):
    if key:
      print(self.brand, 5*'-', '>','Двигатель запущен')
    else:
      print(self.brand, 5*'-', '>','Двигатель остановлен')

  def type_engine(self):
    print(self.brand, 5*'-', '>', self.__engine_type)

  @staticmethod                    #Декоратор статического метода
  def get_count_car():             #Возвращает счетчик объектов класса
    return Car.count

  @classmethod                     #Декоратор классового метода
  def get_color_car(cls):          #Возвращает предустановленный атрибут класса
    return cls.car_color

  @property
  def engine_type(self):
    print("getter method")
    return self.__engine_type

  @engine_type.setter
  def engine_type(self, engine_type):
    print("setter method")
    try:
      index = self.engine_list.index(engine_type)
      self.__engine_type = engine_type
    except ValueError:
      print('Неверный тип двигателя')

  def __repr__(self):
    return f'Car({self.brand!r}: {self.year!r})'

  def __str__(self):
    return '%s: %s' % (self.brand, self.year)

class ElectricCar(Car):
  def __init__(self, brand, year, battery_size):
    super().__init__(brand, year)    # Вызываем конструктор предка
    self.battery_syze = battery_size
    self.__engine_type = 'Электрический'

  def type_engine(self):
    print(self.brand, 5*'-', '>', self.__engine_type)

  def start_engine(self, key=False):
    if key:
      print(self.brand, 5*'-', '>','Тихий старт двигателя')
    else:
      print(self.brand, 5*'-', '>','Двигатель остановлен')

if __name__ == "__main__":
  print('Выполняется в car.py')

  porsche = Car('Porshe 911 Carrena купе', 2017)
  bentley = Car('Bentley Flying Spur седан', 2015)
  ferrari = Car('Ferrari 488 GTB купе', 2016)
  print('Марка авто:', porsche.brand, 5*'-', '>', ' Год выпуска:', porsche.year)
  print('Марка авто:', bentley.brand, 5*'-', '>', ' Год выпуска:', bentley.year)
  print('Марка авто:', ferrari.brand, 5*'-', '>', ' Год выпуска:', ferrari.year)
  print()
  bentley.start_engine(True)
  ferrari.start_engine()
  print()
  bentley.type_engine()
  ferrari.type_engine()
  porsche.type_engine()
  chevrolet = ElectricCar('Chevrolet Bolt хэтчбек', 2019, 60)
  print()
  print('Марка авто:', chevrolet.brand, 5*'-', '>',
        ' Год выпуска:', chevrolet.year, 5*'-', '>',
        ' Мощность двигателя:', chevrolet.battery_syze, 'кВт ч')
  chevrolet.type_engine()
  chevrolet.start_engine(1)
  print()
  print('всего задействовано', Car.get_count_car(), 'авто')
  print()
  print('Предустановленный атрибут: цвет авто', 5*'-', '>',
        ferrari.get_color_car(), 'авто')
  print('Предустановленный атрибут: цвет авто', 5*'-', '>',
        porsche.get_color_car(), 'авто')
  print()
  ferrari.engine_type="Бензиновый"
  print(ferrari.engine_type)
  ferrari.type_engine()
  print()
  bentley.engine_type="бензиновый"
  bentley.engine_type="Бензиновый"
  print()
  print(str(bentley.year))
  print(chevrolet)
