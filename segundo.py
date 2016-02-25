#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier

iris = pd.read_csv('iris.csv')          # Importamos el dataset.
X = iris[['PetalLength', 'PetalWidth']] # Tomamos el ancho y longitud del pétalo.
y = iris['Species'].astype('category')     # Para crear luego los gráficos vamos a necesitar categorizar los nombres
y.cat.categories = [0, 1, 2]  
n_neighbors = 15
step= .02          # step size de la malla

# Creamos los colormap
# cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
# cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # Creamos una instancia de Neighbors Classifier y hacemos un fit a partir de los
    # datos.
    # Los pesos (weights) determinarán en qué proporción participa cada punto en la
    # asignación del espacio. De manera uniforme o proporcional a la distancia.
    clf = KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)
    # Creamos una gráfica con las zonas asignadas a cada categoría según el modelo
    # k-nearest neighborgs. Para ello empleamos el meshgrid de Numpy.
    # A cada punto del grid o malla le asignamos una categoría según el modelo knn.
    # La función c_() de Numpy, concatena columnas.
    x_min = X.iloc[:, 0].min() - 1 
    x_max = X.iloc[:, 0].max() + 1
    y_min = X.iloc[:, 1].min() - 1
    y_max = X.iloc[:, 1].max() + 1

    # Malla de x_min->x_max, y_min->y_max en intervalos de h (steps)
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Ponemos el resultado en un gráfico.
    Z = Z.reshape(xx.shape)


    print xx.min(), xx.max()
    print yy.min(), yy.max()
    print Z

    # plt.figure()
    # plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    # # Representamos también los datos de entrenamiento.


    # plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap=cmap_bold)

    # plt.xlim(xx.min(), xx.max())
    # plt.ylim(yy.min(), yy.max())
    # plt.title("3-Class classification (k = %i, weights = '%s')"
    #           % (n_neighbors, weights))
    # plt.xlabel('Petal Width')
    # plt.ylabel('Petal Length')
    # plt.savefig('iris-knn-{}'.format(weights)) 
