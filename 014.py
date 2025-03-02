"""
Exercício 14 - Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""

import math

area_m2 = int(input('Digite a área em m²: '))
litro = 1 / 3
latas_tinta = 18
preco_lata = 80

qnt_latas = math.ceil(area_m2 * litro / latas_tinta)
preco_total = (qnt_latas * preco_lata)

print(f"Você precisará de {qnt_latas:.2f} latas de tinta e pagará R${preco_total:.2f}")
