################# ИССЛЕДОВАНИЕ ДАННЫХ #####################
from __future__ import absolute_import, division, print_function, unicode_literals

      # импортируем TensorFlow и набор данных TensorFlow
import tensorflow as tf
import tensorflow_datasets as tfds

#tf.logging.set_verbosity(tf.logging.ERROR)

      # вспомогательные библиотеки
import math
import numpy as np
import matplotlib.pyplot as plt

      # Улучшим отображение прогрессбара
import tqdm
import tqdm.auto
tqdm.tqdm = tqdm.auto.tqdm

print(tf.__version__)

#tf.enable_eager_execution()

      # Загружаем набор данных
dataset, metadata = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
train_dataset, test_dataset = dataset['train'], dataset['test']

      # Зададим название классов для использования в модели
class_names = ['Футболка / топ', 'Шорты', 'Свитер', 'Платье',
              'Плащ', 'Сандали', 'Рубашка', 'Кроссовок', 'Сумка',
              'Ботинок']

      # Исследуем данные
num_train_examples = metadata.splits['train'].num_examples
num_test_examples = metadata.splits['test'].num_examples
print('Количество тренировочных экземпляров: {}'.format(num_train_examples))
print('Количество тестовых экземпляров: {}'.format(num_test_examples))
#print(info.features['label'].num_classes)

#print('Метки классов тестовых экземпляров: {}'.format(num_test_examples.target_names))

      # Считываем одно изображение из dadaset
for image, label in test_dataset.take(1):
  break;

      # Получаем данные и метку для выбранного элемента
data = train_dataset.take(1)


      # Выводим информацию о выбранном значении
print(f'Метка: {label}')
print('Данные изображения (вектор):')
print(data)
print(image)
print(label)

      # Преобразуем картинку из набора в картинку размером 28х28
#image = image.numpy().reshape((28, 28))

      # Отрисовка изображения
plt.figure()
plt.imshow(image, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()

      # Так как в изображениях используется 255 градаций серого
      # применим нормализацию и приведем их к значениям (0 - 1)
      # методом деления на 255
def normalize(images, labels):
  images = tf.cast(images, tf.float32)
  images /= 255
  return images, labels

      # Метод map применяет функцию нормализации к каждому элементу в массиве
      # тестовых и тренировочных наборах данных
train_dataset = train_dataset.map(normalize)
test_dataset = test_dataset.map(normalize)

      # Считываем одно изображение из dadaset
for image, label in test_dataset.take(1):
  break;
#print(image)
image = image.numpy().reshape((28, 28))

      # Отрисовка изображения
plt.figure()
plt.imshow(image, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()

      # Отрисуем первуе 25 картинок тестового набора
      # размер картинок 10x10
plt.figure(figsize=(10,10))
i = 0
for (image, label) in test_dataset.take(25):
  image = image.numpy().reshape((28,28))
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(image, cmap=plt.cm.binary)
  plt.xlabel(class_names[label])
  i += 1
plt.show()
print(image)
print(label)

####################################################
