"""
Exercício 36 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento
"""

numero = float(input("Digite um número inteiro: "))

if numero % 1 == 0:
    print(f"{numero} é um número inteiro")
else:
    print(f"{numero} é um número decimal")
