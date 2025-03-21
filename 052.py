"""
Exercício 52 - Altere o programa anterior para mostrar no final a soma dos números.
"""

intervalo = []

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

for i in range(numero_1,numero_2 +1):
    intervalo.append(i)
    
#Tratamento do intervalo para remover os números e manter somente o intervalo    
intervalo.pop(0)
intervalo.pop()

#Soma dos números do intervalo
soma_intervalo = sum(intervalo)

print("O intervalos dos números é: ",intervalo)
print("A soma dos intervalos é: ",soma_intervalo)

