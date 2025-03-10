"""
Exercício 28 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""
dia_semana = int(input("Digite um número correspondete ao dia semana: "))

if dia_semana == 1:
    print("1 - Domingo")
elif dia_semana == 2:
    print("2 - Segunda")
elif dia_semana == 3:
    print("3 - Terça")
elif dia_semana == 4:
    print("4 - Quarto")
elif dia_semana == 5:
    print("5 - Quinta")
elif dia_semana == 6:
    print("6 - Sexta")
elif dia_semana == 7:
    print("7 - Sábado")
else:
    print("Valor inválido")


