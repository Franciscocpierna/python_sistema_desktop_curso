import numpy as np
import pandas as pd
from numpy.random import randn
import pandas as pd


df1 = pd.DataFrame({'Empresa': ['A', 'B', 'C', 'D'],
                   'Setor': ['Bebidas', 'Carnes','Paes','Frutas'],
                   'Vendedor': ['Carlos', 'Marcos', 'Fabiana', 'Juliana'],
                   'Vendas': ['100','200','300','400']},
                  index = [0,1,2,3])

df2 = pd.DataFrame({'Empresa': ['E', 'F', 'G', 'H'],
                   'Setor': ['Legumes', 'Doces','Vinhos','Massas'],
                   'Vendedor': ['Joao', 'Aline', 'Debora', 'Francisco'],
                   'Vendas': ['500','600','700','800']},
                  index = [4,5,6,7])      


df3 = pd.DataFrame({'Empresa': ['I', 'J', 'K', 'L'],
                   'Setor': ['Congelados', 'Importados','Elatados','Almoco'],
                   'Vendedor': ['Telma', 'Rodrigo', 'Carla', 'Jose'],
                   'Vendas': ['900','1000','1100','1200']},
                  index = [8,9,10,11])  

print(df1)     

print()
print()
print(df2) 
print()
print()
print(df3) 

#concatenação
print()
print()
print()
print()
print()

concatena=pd.concat([df1, df2, df3])
print(concatena) 
print()
print()
print()
print()
print()
print(pd.concat([df1,df2,df3], axis = 1))



#Mesclar

esquerda = pd.DataFrame({'Empresa': ['A', 'B', 'C', 'D'],
                   'Setor': ['Bebidas', 'Carnes','Paes','Frutas'],
                   'Vendedor': ['Carlos', 'Marcos', 'Fabiana', 'Juliana'],
                   'Vendas': ['100','200','300','400']})

direita = pd.DataFrame({'Empresa': ['A', 'B', 'C', 'D'],
                   'Setor': ['Legumes', 'Doces','Vinhos','Massas'],
                   'Vendedor': ['Joao', 'Aline', 'Debora', 'Francisco'],
                   'Vendas': ['500','600','700','800']})



print()
print()
print()
print('Mesclar')
print()
print(pd.merge(esquerda, direita, how = 'inner', on = 'Empresa'))                   

print()
print()
print()
print('Juntar')
print()
esquerda = pd.DataFrame({'Setor_A': ['Bebidas', 'Carnes','Paes','Frutas'],
                   'Vendedor_A': ['Carlos', 'Marcos', 'Fabiana', 'Juliana'],
                   'Vendas_A': ['100','200','300','400']},
                    index = ['K0','K1', 'K2', 'K3'])

direita = pd.DataFrame({'Setor_B': ['Legumes', 'Doces','Vinhos','Massas'],
                   'Vendedor_B': ['Joao', 'Aline', 'Debora', 'Francisco'],
                   'Vendas_B': ['500','600','700','800']},
                    index = ['K0','K1', 'K2', 'K3'])

                  
print(esquerda.join(direita))
print()
print()
print()
print('Juntar')
print()

print(esquerda.join(direita, how = 'outer'))