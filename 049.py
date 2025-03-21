"""
Exercício 49 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numeros = []
soma = 0

for i in range(1,6):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)
    
soma = sum(numeros)
media = (soma / len(numeros))

print(f"A soma de dos números é: {soma}")
print(f"A média dos números é: {media}")
