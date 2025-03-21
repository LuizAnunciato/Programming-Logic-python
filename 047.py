"""
Exercício 47 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

for impressao_1 in range(1,21):
    print(impressao_1)

numeros = ''

for impressao_2 in range(1,21):
    numeros += f'{impressao_2},'

print()
print(numeros)
