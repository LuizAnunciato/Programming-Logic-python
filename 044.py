"""
Exercício 43 - Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite seu nome: ")
if len(nome) > 3:
    nome_verificado = nome
else:
    print("Dados inválidos, o nome deve ter mais de 3 caracteres.")
    exit()

idade = int(input("Digite sua idade entre (1 e 150): "))
if 1 <= idade <= 150:
    idade_verificada = idade
else:
    print("Dados inválidos, idade deve estar entre 1 e 150 anos.")
    exit()

salario = float(input("Digite seu salário: "))
if salario > 0:
    salario_verificado = salario
else:
    print("Dados inválidos, salário deve ser maior que R$0,00.")
    exit()

sexo = input("Digite seu sexo (f ou m): ").lower()
if sexo == 'f':
    sexo_verificado = 'Feminino'
elif sexo == 'm':
    sexo_verificado = 'Masculino'
else:
    print("Dados inválidos, sexo deve ser 'f' ou 'm'.")
    exit()

estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()
estados_civis = {'s': 'Solteiro', 'c': 'Casado', 'v': 'Viúvo', 'd': 'Divorciado'}
if estado_civil in estados_civis:
    estado_civil_verificado = estados_civis[estado_civil]
else:
    print("Dados inválidos, estado civil deve ser 's', 'c', 'v' ou 'd'.")
    exit()

# Exibição dos dados válidos
print("\nInformações:")
print()
print(f"Nome: {nome_verificado}")
print(f"Idade: {idade_verificada} anos")
print(f"Salário: R${salario_verificado:.2f}")
print(f"Sexo: {sexo_verificado}")
print(f"Estado Civil: {estado_civil_verificado}")
