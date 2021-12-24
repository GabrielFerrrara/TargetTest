faturamento_mensal = {'SP':67836.43, 'RJ':36678.66, 'MG':29229.88, 'ES':27165.48, 'Outros':19849.53}
total = sum(faturamento_mensal.values())

for key, value in faturamento_mensal.items():
    print(key, round((value/total)*100,2), '%')    

