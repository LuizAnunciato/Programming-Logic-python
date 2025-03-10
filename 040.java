"""
Exercício 40 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
"""

frutas__ate_5kg = {'morango': 2.50,'maçã': 1.80}
frutas_acima_5kg = {'morango': 2.20, 'maçã': 1.50}

fruta = input("Digite qual fruta você irá querer: ").lower()
kg = float(input("Digite a quantidade em KG de fruta: "))

if fruta == 'morango' and kg < 5:
    preco = frutas__ate_5kg['morango']
    preco_total = (preco * kg)
    print()
    print("Informações gerais:")
    print(f"Quantidade em KG: {kg}kg")
    print(f"O valor a ser pago é: R${preco_total:.2f}")
    print()
elif fruta == 'morango' and kg > 5:
    preco = frutas__ate_5kg['morango']
    preco_total = (preco * kg)
    print()
    print("Informações gerais:")
    print(f"Quantidade em KG: {kg}kg")
    print(f"O valor a ser pago é: R${preco_total:.2f}")
    print()

elif fruta == 'maçã' and kg < 5:
    preco = frutas_acima_5kg['maçã']
    preco_total = (preco * kg)
    print()
    print("Informações gerais:")
    print(f"Quantidade em KG: {kg}kg")
    print(f"O valor a ser pago é: R${preco_total:.2f}")
    print()

elif fruta == 'maçã' and kg > 5:
    preco = frutas_acima_5kg['maçã']
    preco_total = (preco * kg)
    print()
    print("Informações gerais:")
    print(f"Quantidade em KG: {kg}kg")
    print(f"O valor a ser pago é: R${preco_total:.2f}")
    print()
else:
    print("Informações inválidas.")
