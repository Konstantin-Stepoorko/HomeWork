############### RGBoost ######################
from __future__ import absolute_import, division, print_function, unicode_literals

### импортируем TensorFlow и набор данных TensorFlow
import tensorflow as tf
import tensorflow_datasets as tfds

# xgboost для классификации
from numpy import asarray
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from xgboost import XGBClassifier
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
xb_cl = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xb_cl.fit(train_im, train_lb)

      # Предсказание
y_pred = xb_cl.predict(test_im)
accuracy = accuracy_score(test_lb, y_pred)
#print(accuracy)                           ### вычисление точности

report = classification_report(test_lb, y_pred)
print(report)
print('='*20)

#====================
#2.15.0
#--------------------
#              precision    recall  f1-score   support
#
#           0       0.84      0.87      0.86      1000
#           1       0.99      0.97      0.98      1000
#           2       0.81      0.83      0.82      1000
#           3       0.90      0.91      0.91      1000
#           4       0.82      0.84      0.83      1000
#           5       0.99      0.97      0.98      1000
#           6       0.74      0.68      0.71      1000
#           7       0.95      0.97      0.96      1000
#           8       0.98      0.98      0.98      1000
#           9       0.96      0.96      0.96      1000
#
#    accuracy                           0.90     10000
#   macro avg       0.90      0.90      0.90     10000
#weighted avg       0.90      0.90      0.90     10000
#
#====================
