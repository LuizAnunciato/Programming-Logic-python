"""
Exercício 37 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

operacao_escolhida = input("Digite a operação desejada, utilizando o operador(+,-,*,/): ")
operacao = {
    '+': numero_1 + numero_2,'-': numero_1 - numero_2,
    '*': numero_1 * numero_2,'/': numero_1 / numero_2}

#Vericações de adição
if operacao_escolhida in operacao and operacao_escolhida == '+':
    calculo = operacao['+']
    print("Resultado: ")
    print(f"{numero_1} + {numero_2} = ",calculo)
    print()
    print("Informações específicas sobre o resultado:")

    if calculo % 2 == 0:
        print(f"{calculo} é um número par")
    else:
        print(f"{calculo} é ímpar")

    if calculo > 0:
        print(f"{calculo} é um número positivo") 
    elif calculo == 0:
        print(f"{calculo} é um número equivalente a zero")
    else:
        print(f"{calculo} é um número negativo")

    if calculo % 1 == 0:
        print(f"{calculo} é um número inteiro")
    else:
        print(f"{calculo} é um número decimal")

#Vericações de subtração
elif operacao_escolhida in operacao and operacao_escolhida == '-':
    calculo = operacao['-']
    print("Resultado:")
    print(f"{numero_1} - {numero_2} = ",calculo)
    print()
    print("Informações específicas sobre o resultado:")

    if calculo % 2 == 0:
        print(f"{calculo} é um número par")
    else:
        print(f"{calculo} é um número ímpar")

    if calculo > 0:
        print(f"{calculo} é um número positivo")
    elif calculo == 0:
        print(f"{calculo} é um número equivalente a zero")
    else:
        print(f"{calculo} é um número negativo")

    if calculo % 1 == 0:
        print(f"{calculo} é um número inteiro")
    else:
        print(f"{calculo} é um número decimal")

#Vericações de multiplicação
elif operacao_escolhida in operacao and operacao_escolhida == '*':
    calculo = operacao['*']
    print("Resultado:")
    print(f"{numero_1} * {numero_2} = ",calculo)
    print()
    print("Informações específicas sobre o resultado:")

    if calculo % 2 == 0:
        print(f"{calculo} é um número par")
    else:
        print(f"{calculo} é um número ímpar")

    if calculo > 0:
        print(f"{calculo} é um número positivo")
    elif calculo == 0:
        print(f"{calculo} é um número equivalente a zero")
    else:
        print(f"{calculo} é um número negativo")
    
    if calculo % 1 == 0:
        print(f"{calculo} é um número inteiro")
    else:
        print(f"{calculo} é um número decimal")

#Vericações de divisão
elif operacao_escolhida in operacao and operacao_escolhida == '/':
    calculo = operacao['/']
    print("Resultado:")
    print(f"{numero_1} / {numero_2} = ",calculo)
    print()
    print("Informações específicas sobre o resultado:")

    if calculo % 2 == 0:
        print(f"{calculo} é um número par")
    else:
        print(f"{calculo} é um número ímpar")
    
    if calculo > 0:
        print(f"{calculo} é um número positivo")
    elif calculo == 0:
        print(f"{calculo} é um número equivalente a zero")
    else:
        print(f"{calculo} é um número negativo")

    if calculo % 1 == 0:
        print(f"{calculo} é um número inteiro")
    else:
        print(f"{calculo} é um número decimal")

else:
    print("Operação inválida.")
