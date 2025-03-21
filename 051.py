"""
Exercício 51 - Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""

intervalo = []

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

for i in range(numero_1,numero_2 +1):
    intervalo.append(i)
    
#Tratamento da lista para remover os números e manter somente o intervalo    
intervalo.pop(0)
intervalo.pop()

print(O intervalos dos números é: ",intervalo)



