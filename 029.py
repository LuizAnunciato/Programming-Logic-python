"""
Exercício 29 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E

O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.
"""

disciplina = input("Digite a disciplina que você deseja saber sua média: ")

b1 = float(input("Digite a nota da B1: "))
b2  = float(input("Digite a nota da B2: "))
media = (b1 + b2) / 2

if (media > 9.0 and media <= 10.0):
    conceito = 'A'
    print(f"Sua média na disciplina de {disciplina} é: {media:.2f}, você se encontra no conceito {conceito}")
elif (media >= 7.5 and media < 9.0):
    conceito = 'B'
    print(f"Sua média na disciplina de {disciplina} é: {media:.2f}, você se encontra no conceito {conceito}")
elif (media >= 6.0 and media < 7.5):
    conceito = 'C'
    print(f"Sua média na disciplina de {disciplina} é: {media:.2f}, você se encontra no conceito {conceito}")
elif (media >= 4.0 and media < 6.0):
    conceito = 'D'
    print(f"Sua média na disciplina de {disciplina} é: {media:.2f}, você se encontra no conceito {conceito}")
elif (media < 4.0):
    conceito = 'E'
    print(f"Sua média na disciplina de {disciplina} é: {media:.2f}, você se encontra no conceito {conceito}")
else:
    print("Digite uma nota válida")


if conceito in ['A', 'B', 'C']:
    print("Você foi aprovado✅")
else:
    print("Você foi reprovado❌")
