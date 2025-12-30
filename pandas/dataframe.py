import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4), index ='A B C D E'.split(), columns = 'W X Y Z'.split())

print(df)
print(df['W'])
print(df.loc['A'])

# Valor da linha 'A' na coluna 'W'
print(df.loc['A', 'W'])

###Seleção e indexação

print(df[['W', 'Z']])

print(df.X)

print(df)


df['Novo'] = df['W'] - df['X']
print(df['Novo'])
#df = df.drop('Novo', axis=1)
print(df)
#df = df.drop('C', axis=0)
print(df)

df = pd.DataFrame(randn(5,4), index ='A B C D E'.split(), columns = 'W X Y Z'.split())
print(df)

print(df.iloc[2])
print(df)
print(df.iloc[2])
print(df)
#traz  a celula A W  0,302665 
print(df.loc['A', 'W'])
print(df)
#retorna parte do dataframe

df2 = df.loc[['A', 'B', 'C'], ['X','Y']]
print(df2)
print(df>0)
print(df[df>0])
print()
print()
print(df[df['X'] > 0])