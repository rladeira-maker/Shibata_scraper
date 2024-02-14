#!/usr/bin/env python3
import os
import pandas as pd

MERCADOS = pd.read_csv('Mercados_24_02_13.csv')
MERCADOS.PRODUTO = MERCADOS.PRODUTO.str.lower()
SEARCH = input('Qual produto procura? ')
if SEARCH == '':
    os.sys.exit()
MSG = 'Qual o método de ordenação: preço FINAL, por QUILO ou por LITRO? '
METODO = input(MSG)
if METODO.upper() == 'FINAL':
    METODO = 'PRECO-FINAL'
elif METODO.upper() == 'QUILO':
    METODO = 'PRECO/KG'
elif METODO.upper() == 'LITRO':
    METODO = 'PRECO/L'
else:
    os.sys.exit()

LST_SEARCH = SEARCH.lower().split()
PATTERN = r'^'+LST_SEARCH[0]
LST_SEARCH[0] = ''

for item in LST_SEARCH:
    PATTERN = PATTERN + item + '.*'

MERCADOS = MERCADOS[MERCADOS.PRODUTO.str.contains(PATTERN)]
print((MERCADOS).sort_values(by=METODO).head())

if not os.path.isfile('lista.csv'):
    TEMPDF = pd.DataFrame(columns=['ID', 'PRODUTO', 'PRECO-FINAL',
                                   'PRECO-CHEIO', 'PRECO/KG', 'PRECO/L',
                                   'SECAO', 'MERCADO'])
    TEMPDF.to_csv('lista.csv', index=False)

DF = pd.read_csv('lista.csv')
# print(DF)
MERCADOS = pd.concat([DF, MERCADOS.sort_values(by=METODO).head()])
# print(MERCADOS)
MERCADOS.sort_values(by=['PRECO-FINAL', 'PRODUTO']).to_csv('lista.csv',
                                                           index=False)
