"""
Exercício 55 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""

numeros_pares = []
numeros_impares = []

for i in range(1,11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else: 
        numeros_impares.append(numero)

quantidade_numeros_pares = len(numeros_pares)
quantidade_numeros_impares = len(numeros_impares)

print()
print(f"{quantidade_numeros_pares} são números pares")
print(f"{quantidade_numeros_impares} são números ímpares")
  
    

    
