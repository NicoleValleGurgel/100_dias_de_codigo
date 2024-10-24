import pandas as pd
import numpy as np

data = {'vendas': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]}
df = pd.DataFrame(data)

# Operacoes
media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

# Resultados
print('Média:', media)
print('Median:', mediana)
print('Desvio padrao:', desvio_padrao)
print('Maximo:', maximo)
print('Minimo:', minimo)