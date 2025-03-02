"Exercício 11 - Tendo como dado de entrada a altura (h) de uma pessoa,
"construa um algoritmo que calcule seu peso ideal,"
"utilizando as seguintes fórmulas:
    "Para homens: (72.7*h) - 58"
    "Para mulheres: (62.1*h) - 44.7"

nome = input("Digite seu nome: ")
genero = input("Digite seu gênero (h ou m): ")
altura = float(input("Digite sua altura: "))

if genero == 'h':
    peso_ideal = ((72.7*altura) - 58)
elif genero == 'm':
    peso_ideal = ((62.1*altura) - 44.7)
else:
    genero = None
    print("Gênero inválido")


print(f"Seu peso ideal é {peso_ideal:.2f}kg")
