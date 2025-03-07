"""
Exercício 35 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão)
"""

numero = int(input("Digite um número para verificar se ele é (par) ou (ímpar): "))

if (numero % 2 == 0):
    print(f"{numero} é um número PAR")
else:
    print(f"{numero} é um número ÍMPAR")

