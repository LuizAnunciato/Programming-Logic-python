"""
Exercício 31 - Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c.

O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
"""

# Equação do 2º grau

a = float(input("Digite o valor de A: "))

if a == 0:
    print("Essa equação não é do segundo grau e não será executada")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    # Cálculo do delta
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Essa equação não possui raízes reais e não será executada")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Essa equação possui apenas uma raiz real: x = {x:.2f}")
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}")
