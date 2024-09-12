# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# * SP – R$67.836,43
# * RJ – R$36.678,66
# * MG – R$29.229,88
# * ES – R$27.165,48
# * Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  


import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento_total= 0.0
valorTotal = 0.0
dict_estados = [
    {"estado": "SP", "valor": 67836.43},
    {"estado": "RJ", "valor": 36678.66},
    {"estado": "MG", "valor": 29229.88},
    {"estado": "ES", "valor": 27165.48},
    {"estado": "Outros", "valor": 19849.53}
]

for item in dados:
  valor = item['valor']
  if valor is not None:
    faturamento_total += valor

percentuais = {item["estado"]: (item["valor"] / faturamento_total) * 100 for item in dict_estados}
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")