import pandas as pd
import numpy as ny

# carregar o CSV

df = pd.read_csv("clientes.csv")

# remover as linhas duplicadas

df = df.drop_duplicates()

#tratar dados ausentes
# preencher salários ausentes com a média da coluna
df["salario"] = df["salario"].fillna(df["salario"].mean())

#remover as outliers

df = df[df["idade"].between(0,100)]

# criar faixa salarial

# salvar as informações em um novo arquivo CSV tratado

df.to_csv("clientes_tratados.csv", index=False)