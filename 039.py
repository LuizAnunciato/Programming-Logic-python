"""
Exercício 39 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

print("A - Álcool")
print("G - Gasolina")
print()

combustivel = input("Digite o combustível que você deseja: ").upper()

# Preços por litro
preco_litro_alcool = 1.90
preco_litro_gasolina = 2.50

if combustivel == 'A':
    alcool = float(input("Digite quantos litros de Álcool você adquiriu: "))

    # Define o percentual de desconto
    desconto_percentual = 0.03 if alcool <= 20 else 0.05

    # Calcula o valor total com desconto
    preco_sem_desconto = alcool * preco_litro_alcool
    preco_total = preco_sem_desconto * (1 - desconto_percentual)

    print(f"Você irá pagar R$ {preco_total:.2f} por {alcool} litros de Álcool.")

elif combustivel == 'G':
    gasolina = float(input("Digite quantos litros de Gasolina você adquiriu: "))

    # Define o percentual de desconto
    desconto_percentual = 0.04 if gasolina <= 20 else 0.06

    # Calcula o valor total com desconto
    preco_sem_desconto = gasolina * preco_litro_gasolina
    preco_total = preco_sem_desconto * (1 - desconto_percentual)

    print(f"Você irá pagar R$ {preco_total:.2f} por {gasolina} litros de Gasolina.")

else:
    print("Elemento inválido. Programa encerrado.")

