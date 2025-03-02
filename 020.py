"""
Exercício 20 -
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

b1 = float(input("Digite sua nota b1: "))
b2 = float(input("Digite sua nota b2: "))

media = (b1+b2) / 2

if media >= 7 and media <10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com distinção")
elif media < 7:
    print("Reprovado")
