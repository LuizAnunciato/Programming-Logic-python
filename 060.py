"""
Exercício 60 - Altere o programa de cálculo dos números primos, informando, caso o número não
seja primo, por quais número ele é divisível.
"""
numero = int(input("Digite um número para verificar se é primo ou não: "))

if numero <= 1:
    print(f"{numero} não é um número primo.")
else:
    primo = True
    for i in range(2, numero):
        if numero % i:
            primo = False
            break
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
        for x in range(2, numero):
            if numero % x == 0:
                print(f"{x} é um divisor de {numero}")
                break
            else:
                print(f"{x} não é um divisor de {numero}")
