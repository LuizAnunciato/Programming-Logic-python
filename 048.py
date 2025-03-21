"""
Exercício 48 - Faça um programa que leia 5 números e informe o maior número.
"""

numeros = []

for i in range(1,6):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

maior_numero = max(numeros)
print(maior_numero)   
