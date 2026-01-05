import pandas as pd
import seaborn as sns

print()
print()
print()
print('### Dataframe tips')
print('df = sns.load_dataset("tips")')
df = sns.load_dataset('tips')
print(df)

print()
print()
print()
print('### Dataframe tips')
print('df = pd.concat([df.head(), df.tail()])')

df = pd.concat([df.head(), df.tail()])

print(df)
print()
print()
print()
print('### Dataframe tips')
print('df.info()')

print(df.info())

print(df)
print()
print()
print()
print('### Dataframe tips')
print('df.describe()')

print(df.describe())

print()
print()
print()
print('### ### Salvar dataframe como CSV')
print('df.to_csv(endereço do arquivo tips_dataframe.csv, index = False, header = True')

df.to_csv('tips_dataframe.csv', index = False, header = True)
print()
print()
print()
print('### Leitura de CSV')
print('df = pd.read_csv("endereco arquivo tips_dataframe.csv")')

df = pd.read_csv('tips_dataframe.csv')

print()
print()
print()
print('### df.head()')
print('df.head()')


print(df.head())

print()
print()
print()
print('### Seaborn e Matplotlib')
print('sns.jointplot(x = "total_bill", y = "tip", data = df, kind = "reg")')
print()
print()
print()
sns.jointplot(x = 'total_bill', y = 'tip', data = df, kind = 'reg')

