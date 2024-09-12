# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# * O menor valor de faturamento ocorrido em um dia do mês;
# * O maior valor de faturamento ocorrido em um dia do mês;
# * Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# * SP – R$67.836,43
# * RJ – R$36.678,66
# * MG – R$29.229,88
# * ES – R$27.165,48
# * Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  


import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

with open('dados.json', 'r') as file:
    dados = json.load(file)


maior_valor = None
dia_maior_valor = None
menor_valor = None
dia_menor_valor = None

faturamento_total= 0.0
media_mensal = 0.0


for item in dados:
  valor = item['valor']
  if valor is not None:
    faturamento_total += valor

  media_mensal = faturamento_total/30

  if maior_valor is None or valor > maior_valor:
     maior_valor = valor
     dia_maior_valor = item['dia']

  if menor_valor is None or valor < menor_valor and valor != 0.0:
     menor_valor = valor
     dia_menor_valor = item['dia']


dias_acima_media = {item["dia"]: locale.currency(item["valor"], grouping=True) for item in dados if item["valor"] > media_mensal}

print("=" * 40)
print(f"O maior valor é {locale.currency(maior_valor, grouping=True)} no dia {dia_maior_valor}.")
print(f"O menor valor é {locale.currency(menor_valor, grouping=True)} no dia {dia_menor_valor}.")
print(f"O faturamento total é {locale.currency(faturamento_total, grouping=True)}")

print("=" * 40)
print(f"Media mensal: {locale.currency(media_mensal, grouping=True)}")
for dia, valor in dias_acima_media.items():
   print(f"- Dia {dia} :  {valor}")