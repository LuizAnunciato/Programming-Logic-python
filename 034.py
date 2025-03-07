"""
Exercício 34 - Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.

O programa não deve se preocupar com a quantidade de notas existentes na
máquina.

Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

saque = float(input("Digite o valor do saque: "))
notas = [100,50,10,5,1]

if saque < 10:
    print("O saque mínimo é R$10,00")
elif saque > 600:
    print("O saque máximo é R$600,00")
else:
    print("Notas fornecidas: ")
    for nota in notas:
        qtd_notas = saque // nota
        saque %= nota
        if qtd_notas > 0:
            print(f"{int(qtd_notas)} nota(s) de R${nota},00")
