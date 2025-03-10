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
  
# Dicionários com os preços
frutas_ate_5kg = {'morango': 2.50, 'maçã': 1.80}
frutas_acima_5kg = {'morango': 2.20, 'maçã': 1.50}

# Entrada de dados
morango_kg = float(input("Digite a quantidade de Morangos (kg): "))
maca_kg = float(input("Digite a quantidade de Maçãs (kg): "))

# Definir preço por kg conforme a quantidade comprada
preco_morango_kg = frutas_ate_5kg['morango'] if morango_kg <= 5 else frutas_acima_5kg['morango']
preco_maca_kg = frutas_ate_5kg['maçã'] if maca_kg <= 5 else frutas_acima_5kg['maçã']

# Calcular o preço total
preco_morango = morango_kg * preco_morango_kg
preco_maca = maca_kg * preco_maca_kg
valor_total = preco_morango + preco_maca
peso_total = morango_kg + maca_kg

# Aplicação do desconto de 10% se o total passar de 8kg ou R$ 25,00
if peso_total > 8 or valor_total > 25:
    valor_total *= 0.90  # Aplica 10% de desconto

# Exibição do resultado
print("\nInformações gerais:")
print(f"Quantidade de Morango: {morango_kg:.2f} kg")
print(f"Quantidade de Maçã: {maca_kg:.2f} kg")
print(f"Valor total: R$ {valor_total:.2f}")


