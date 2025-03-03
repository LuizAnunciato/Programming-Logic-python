"""
"Exercício 23 - Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato
"""

preco_produto_1 = float(input("Digite o valor a ser pago no produto 1: "))
preco_produto_2 = float(input("Digite o valor a ser pago no produto 2: "))
preco_produto_3 = float(input("Digite o valor a ser pago no produto 3: "))

if preco_produto_1 < preco_produto_2 and preco_produto_1 < preco_produto_3:
    print(f"Você deverá comprar o produto 1, pois está apenas R${preco_produto_1:.2f}")
elif preco_produto_2 < preco_produto_1 and preco_produto_2 < preco_produto_3:
    print(f"Você deverá comprar o produto 2, pois está apenas R${preco_produto_2:.2f}")
else:
    print(f"Você deverá comprar o produto 3, pois está apenas R${preco_produto_3:.2f}")
