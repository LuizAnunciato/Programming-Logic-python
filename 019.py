"""
Exercício 19 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

vogais = 'AEIOU'
consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'

letra = input("Digite um letra: ")

if letra.upper() in vogais:
    print("A letra digitada é uma vogal")
elif letra.upper() in consoantes:
    print("A letra digitada é uma consoante")
else:
    print("Caractere inválido")

