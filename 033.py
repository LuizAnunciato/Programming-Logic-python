"""
Exercício 33 - 
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.
"""
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

mes_30 = [4, 6, 9, 11]  # Meses com 30 dias
mes_31 = [1, 3, 5, 7, 8, 10, 12]  # Meses com 31 dias

# Validação do mês
if mes < 1 or mes > 12:
    print("O elemento mês é inválido.")
# Validação do dia para meses com 31 dias
elif mes in mes_31 and (dia < 1 or dia > 31):
    print("O dia é inválido para este mês.")
# Validação do dia para meses com 30 dias
elif mes in mes_30 and (dia < 1 or dia > 30):
    print("Esse mês tem apenas 30 dias.")
# Validação para fevereiro (mês 2)
elif mes == 2:
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if bissexto and (dia < 1 or dia > 29):  # Ano bissexto: 29 dias
        print("Fevereiro tem apenas 29 dias em anos bissextos.")
    elif not bissexto and (dia < 1 or dia > 28):  # Ano não bissexto: 28 dias
        print("Fevereiro tem apenas 28 dias em anos não bissextos.")
    else:
        print("Data válida.")
else:
    print("Data válida.")
