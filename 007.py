"Exercício 7 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius."
"Fórmula: C = 5 * ((F-32) / 9)"

F = float(input("Digite o valor da temperatura em (Fº) para ser transformada em (Cº): "))
C = (5 * (F-32) / 9)

print(f"{F} graus Fahrenheit em graus Celsius é: {C:.2f}")

