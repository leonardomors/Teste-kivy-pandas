import pandas as pd

excel = pd.read_excel("teste.xlsx")
print(excel['text'][0])
excel['text'][0] = 'full'
print(excel)