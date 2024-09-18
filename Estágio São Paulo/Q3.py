#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
# que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


#não achei o json ou xml então resolvi criar um eu mesmo. Além disso ignorei os dias sem faturamento também para o calculo 
#do valor mínimo e máximo, pois caso não fizesse isso o valor mínimo seria sempre 0

import json

with open('Estágio São Paulo/dados.json', 'r') as arquivo_json:
    faturamento = json.load(arquivo_json)["faturamento_diario"]

faturamento_valido = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([dia for dia in faturamento_valido if dia > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Média mensal de faturamento: {media_mensal}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")