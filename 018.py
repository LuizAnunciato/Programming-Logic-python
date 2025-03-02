"""
Exercício 18 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = input("Digite o seu sexo: ").format().upper()

if sexo == 'M':
    print("Masculino")
elif sexo == 'F':
    print("Feminino")
else:
    print("Sexo Inválido")

