"""
Exercício 38 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

nome = input("Digite seu nome: ")

#5 perguntas referente ao crime
pergunta_1 = input("Telefonou para vítmima? (Sim ou Não): ").lower()
pergunta_2 = input("Esteve no local do crime? (Sim ou Não): ").lower()
pergunta_3 = input("Mora perto da vítima? (Sim ou Não): ").lower()
pergunta_4 = input("Devia para vítima? (Sim ou Não): ").lower()
pergunta_5 = input("Já trabalhou com a vítima? (Sim ou Não): ").lower()

positivos = 0

if pergunta_1 == 'sim':
    positivos += 1

if pergunta_2 == 'sim':
    positivos += 1

if pergunta_3 == 'sim':
    positivos += 1

if pergunta_3 == 'sim':
    positivos += 1

if pergunta_4 == 'sim':
    positivos += 1

if pergunta_5 == 'sim':
    positivos += 1


if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeita")
elif positivos < 5:
    print("Cúmplice")
else:
    print("Assassino")
