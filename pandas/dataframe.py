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

#dados ausentes em pandas



df = pd.DataFrame({'A':[10 ,20 , np.nan],
                   'B':[40, np.nan, np.nan],
                   'C':[70, 80, 90]})

print(df)                   

print(df.dropna(axis=1))

print(df.dropna(axis=0))
print()
print(df) 
print(df.dropna(thresh=2))

print(df.fillna(value = 'correto'))
print()
print()
print(df)

print()
print(df['A'].fillna(value = df['A'].mean())) #traz a media na coluna A  das 2 linhas e joga na terceira linha
#GroupBy
print()
print()
print()
dados= {'Setor': ['Frutas', 'Frutas', 'Bebidas', 'Bebidas', 'Carnes', 'Carnes'],
        'Vendedores': ['Alice', 'Carlos', 'Aline', 'João', 'Flavia', 'João'],
        'Venda': [100, 200, 300, 400, 500, 600]}

df = pd.DataFrame(dados)
print(df)    
print()
print(df.groupby('Setor'))

setor = df.groupby('Setor')
print(setor.min())

print()
print(setor.mean(numeric_only=True))

print(setor.std(numeric_only=True))

print(setor.max())

print(setor.count())

print(sum(df['Venda'])) 

print(df.info())
print(df.head())
print(df.describe())
