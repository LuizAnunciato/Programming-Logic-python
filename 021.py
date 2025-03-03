"""
"Exercício 21 - Faça um Programa que leia três números e mostre o maior deles
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("O maior número é: ",numero_1)
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("O maior número é: ",numero_2)
else:
    print("O maior número é: ",numero_3)
