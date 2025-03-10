"""
Exercício 43 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
"""

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha (apenas caracteres): ")

while senha == usuario:
    print("Erro, nome de usuário não pode ser semelhante a senha.")
    usuario = input("Digite seu nome de usuário novamente: ")
    senha = input("Digite sua senha novamente (apenas caracteres)")

print("Acesso concedido.")
