
#apelidos alias para as bibliotecas
import pandas as pd
import numpy as np

numeros_impares = [43,55,1,3,11,27,109]
numeros_seq = [2,3,4,3,6,3,8]
print(type(numeros_impares))

serie_impares = pd.Series(numeros_impares)
print(serie_impares)
print(type(serie_impares))

print (serie_impares[3])

print(serie_impares.sum())
print(serie_impares.mean()) #média aritmética
print(serie_impares.min())
print(serie_impares.max())
print(len(serie_impares))
print((serie_impares.describe()))
print((serie_impares[serie_impares > 50]))

serie2_impares = pd.Series(numeros_impares, index=['a','b','c','d','e','f','g'])
print(serie2_impares)


