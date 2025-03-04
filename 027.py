"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

#Cálculo da Folha de pagamento

valor_hora = int(input("Digite o valor da sua hora trabalhada: "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas nesse mês: "))

salario_bruto = (valor_hora * qtd_horas)

#Descontos do IR
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 0.05
elif salario_bruto <= 2500:
    ir = 0.10
else:   
    ir = 0.20

#Desconto total do IR
desconto_ir = salario_bruto * ir

#Desconto INSS
inss = 0.10

#Desconto FGTS
fgts = 0.11

#Desconto total
total_descontos = (salario_bruto * ir + salario_bruto * inss) 

#Salário líquido
salario_liquido = (salario_bruto - total_descontos)

#Impressão salário bruto
print(f"Salário bruto: ({valor_hora} * {qtd_horas})     : R${salario_bruto:.2f}")

#Impressão Desconto do IR
print(f"(-) IR ({ir * 100:.0f}%)                  : R${desconto_ir:.2f}")

#Impressão Desconto INSS
print(f"(-) INSS ({inss * 100:.0f}%)               : R${salario_bruto * inss:.2f}")

#Impressão Desconto FGTS
print(f"(-) FGTS ({fgts * 100:.0f}%)               : R${salario_bruto * fgts:.2f}")

#Impressão Total de descontos
print(f"Total de descontos           : R${total_descontos:.2f}")

#Impressão Salário líquido
print(f"Salário líquido              : R${salario_liquido:.2f}")

