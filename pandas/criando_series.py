import numpy as np
import pandas as pd


lista1=['a', 'b', 'c']
lista2=[1, 2, 3]
arr = np.array([10, 20, 30])
d = {'a': 100,'b': 200, 'c': 300}
serie = pd.Series(data = lista2, index = lista1)
print(serie)
print(serie['a'])
serie = pd.Series(lista2, lista1)
print(f'a serie é \n{serie}') 
serie1 = pd.Series(arr, lista1)
print(f"a sere1 é \n{serie1}")
serie2 = pd.Series(arr)
print(f"a sere2 é \n{serie2}")
serie2 = pd.Series(d)
print(f"a sere2 é \n{serie2}")

serie3 = pd.Series([1,2,3,4], ['João', 'Maria', 'Pedro', 'Carlos'])
print(f'a serie3 \n{serie3}')
print(serie3['João'])
print(serie2+ serie3)
lista2=[1, 2, 3,4]
print(serie3+lista2) 