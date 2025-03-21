"""
Exercício 45 - Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

populacao_a = 80000
populacao_b = 200000

taxa_crescimento_a = 0.03
taxa_crescimento_b = 0.015

anos = 0

while populacao_a < populacao_b:
    populacao_a += taxa_crescimento_a * populacao_a
    populacao_b += taxa_crescimento_b * populacao_b
    anos += 1

print("A quantidade de anos que a população A irá ultrapassar a populaçãio B é: ", anos)
