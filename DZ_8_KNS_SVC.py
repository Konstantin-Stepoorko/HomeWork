from __future__ import absolute_import, division, print_function, unicode_literals

      # импортируем TensorFlow и набор данных TensorFlow
import tensorflow as tf
import tensorflow_datasets as tfds

      # вспомогательные библиотеки
import math
import numpy as np
import matplotlib.pyplot as plt


(train_im, train_lb), (test_im, test_lb) = tfds.as_numpy(tfds.load('fashion_mnist', split = ['train', 'test'], batch_size=-1, as_supervised=True))

print("Размерность данных: ", train_im.data.shape)

train_im = train_im / 255.0
test_im = test_im /  255.0

train_im = train_im.reshape(len(train_im), -1)
test_im = test_im.reshape(len(test_im), -1)

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

################# Обучение модели (метод ближайших соседей)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(train_im, train_lb)

# Оценка модели
y_pred = model.predict(test_im)
accuracy = accuracy_score(test_lb, y_pred)
print(f"Точность модели: {accuracy}")

# Отчет о классификации
classification_rep = classification_report(test_lb, y_pred)
print(classification_rep)

#Размерность данных:  (60000, 28, 28, 1)
#Точность модели: 0.8541
#              precision    recall  f1-score   support
#
#           0       0.76      0.85      0.80      1000
#           1       0.98      0.97      0.98      1000
#           2       0.72      0.81      0.76      1000
#           3       0.91      0.85      0.88      1000
#           4       0.80      0.74      0.77      1000
#           5       0.99      0.83      0.91      1000
#           6       0.65      0.59      0.62      1000
#           7       0.89      0.95      0.92      1000
#           8       0.98      0.95      0.97      1000
#           9       0.89      0.97      0.93      1000
#
#    accuracy                           0.85     10000
#   macro avg       0.86      0.85      0.85     10000
#weighted avg       0.86      0.85      0.85     10000


################## Метод SVC
# Обучение модели (Support Vector Classifier) из модели SVM
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

svc_model = svm.SVC()
svc_model.fit(train_im, train_lb)

# Оценка модели
y_pred = svc_model.predict(test_im)
accuracy = accuracy_score(test_lb, y_pred)
print(f"Точность модели: {accuracy}")

# Отчет о классификации
classification_rep = classification_report(test_lb, y_pred)
print(classification_rep)

#Точность модели: 0.8829
#              precision    recall  f1-score   support
#
#           0       0.83      0.86      0.84      1000
#           1       0.99      0.96      0.98      1000
#           2       0.79      0.82      0.80      1000
#           3       0.87      0.89      0.88      1000
#           4       0.81      0.81      0.81      1000
#           5       0.96      0.95      0.96      1000
#           6       0.72      0.66      0.69      1000
#           7       0.93      0.95      0.94      1000
#           8       0.97      0.98      0.97      1000
#           9       0.96      0.95      0.96      1000
#
#    accuracy                           0.88     10000
#   macro avg       0.88      0.88      0.88     10000
#weighted avg       0.88      0.88      0.88     10000
