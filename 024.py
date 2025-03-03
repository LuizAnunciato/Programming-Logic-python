"""
"Exercício 24 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

numeros = [numero_1,numero_2,numero_3]
numeros.sort(reverse=True)
print(numeros)

