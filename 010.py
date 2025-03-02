"Exercício 10 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal"
"usando a seguinte fórmula: (72.7*altura) - 58"

altura = float(input("Digite sua altura: "))
peso = ((72.7 * altura) - 58)

print(f"levando em consideração a sua altura de {altura}m, o seu peso ideal é de {peso:.2f}kg")


