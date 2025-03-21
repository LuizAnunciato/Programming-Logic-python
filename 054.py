"""
Exercício 54 - Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

print("Vamos trabalhar com potenciação")
print()

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for i in range(0,expoente):
    resultado *= base

print(f"{base} elevado a {expoente} = {resultado}")
