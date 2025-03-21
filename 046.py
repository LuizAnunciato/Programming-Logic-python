"""
Exercício 46 - Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""

populacao_a = int(input("Digite a população de A: "))
populacao_b = int(input("Digite a população B: "))

taxa_crescimento_a = float(input("Digite a taxa de crescimento da população A: "))
taxa_crescimento_b = float(input("Digite a taxa de crescimento da população B: "))

anos = 0

taxa_crescimento_a /= 100
taxa_crescimento_b /= 100

if populacao_a < populacao_b:
    while populacao_a < populacao_b:
        populacao_a += taxa_crescimento_a * populacao_a
        populacao_b += taxa_crescimento_b * populacao_b
        anos += 1

print("A quantidade de anos que a população A irá ultrapassar a populaçãio B é: ", anos)
