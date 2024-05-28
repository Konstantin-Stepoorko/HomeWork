############### LightGBM ######################
from __future__ import absolute_import, division, print_function, unicode_literals

### импортируем TensorFlow и набор данных TensorFlow
import tensorflow as tf
import tensorflow_datasets as tfds

# LightGBM для классификации
from numpy import asarray
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
import lightgbm as lgb
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import classification_report, accuracy_score

############### Программа ###########################
print('='*20)
print(tf.__version__)
print('-'*20)

### Загружаем набор данных
(train_im, train_lb), (test_im, test_lb) = tfds.as_numpy(tfds.load('fashion_mnist', split = ['train', 'test'], batch_size=-1, as_supervised=True))

### Предобработка данных
      # Нормализация
train_im = train_im / 255.0
test_im = test_im /  255.0
      # Преобразование в вектор
train_im = train_im.reshape(len(train_im), -1)
test_im = test_im.reshape(len(test_im), -1)

      # Обучение
lgb_cl = lgb.LGBMClassifier(num_leaves=31, learning_rate=0.05, n_estimators=100)
lgb_cl.fit(train_im, train_lb)

      # Предсказание
y_pred = lgb_cl.predict(test_im)
accuracy = accuracy_score(test_lb, y_pred)        ### вычисление точности
print(accuracy)


report = classification_report(test_lb, y_pred)
print(report)
print('='*20)

#===================
#0.8877
#              precision    recall  f1-score   support
#
#           0       0.83      0.85      0.84      1000
#           1       0.99      0.97      0.98      1000
#           2       0.79      0.82      0.81      1000
#           3       0.88      0.90      0.89      1000
#           4       0.80      0.82      0.81      1000
#           5       0.99      0.97      0.98      1000
#           6       0.71      0.64      0.68      1000
#           7       0.94      0.97      0.96      1000
#           8       0.97      0.97      0.97      1000
#           9       0.96      0.96      0.96      1000
#
#    accuracy                           0.89     10000
#   macro avg       0.89      0.89      0.89     10000
#weighted avg       0.89      0.89      0.89     10000
#
#====================
