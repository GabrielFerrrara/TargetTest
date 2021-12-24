import json

with open("dados.json") as dados_json:
    dados = json.load(dados_json)

total = sum(valores['valor'] for valores in dados )

contador = 0
menor = 0
maior = 0
for unitario in dados:
    if(float(unitario['valor']) != 0):
        if(contador == 0):
            menor = unitario['valor']
            maior = unitario['valor']
        elif(unitario['valor'] < menor):
            menor = unitario['valor']
        elif(unitario['valor'] > maior):
            maior = unitario['valor']
        
        contador += 1

media = round(total/contador,4)

dias_menor = []
qnt_dias = 0
for unitario in dados:
    if(float(unitario['valor']) > media):
        dias_menor.append(unitario['dia'])
        qnt_dias += 1

print('O menor valor de faturamento ocorrido em um dia do mês (excluindo os s/ faturamento): ', menor)
print('O maior valor de faturamento ocorrido em um dia do mês: ', maior)
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:', qnt_dias, ',sendo eles: \n', dias_menor)