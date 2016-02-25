#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pandas import read_csv
iris = read_csv('iris.csv')
iris = iris[iris.Species != 'setosa']
virginica = iris.Species=='virginica'
features = iris.columns[1:5]
best_acc = 0.0
for fi in features:                    # Por cada parámetro o característica de la que tenemos valores
    thresh = iris[fi].copy()           # obtenemos una lista de valores para el umbral
    thresh.sort_values(inplace=True)          # que ordenamos de menor a mayor.
    for t in thresh:                   # Por cada posible valor de umbral
        pred = (iris[fi] > t)       # determinamos los elementos de la tabla que están por encima
        acc = (pred==virginica).mean() # y calculamos que porcentaje de la familia virginica está recogida.
        if acc > best_acc:          # Si mejoramos la detección, actualizamos los parámetro de la colección.
            best_acc = acc             # Mejor precisión obtenida.
            best_fi = fi               # Mejor característica para clasificar las familias.
            best_t = t                 # Valor óptimo de umbral.


print best_acc, best_fi, best_t
