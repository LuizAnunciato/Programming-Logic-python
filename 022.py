"""
"Exercício 22 - Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

if numero_1 < numero_2 and numero_1 < numero_3:
    print(f"O número {numero_1} é o menor")
elif numero_2 < numero_1 and numero_2 < numero_3:
    print(f"O número {numero_2} é o menor")
else:
    print(f"O número {numero_3} é o menor")
