"""
Exercício 12 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
salario_hora = float(input("Digite o valor da sua hora de trabalho: "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas nesse mês: "))

#Calculo do salario total bruto
salario_bruto = (salario_hora * qtd_horas)
print(f"O seu salário bruto é de R${salario_bruto:.2f} nesse mês")

#Calculo do imposto de renda
ir = salario_bruto * (0.11)
print(f"O valor pago de imposto de renda é de R${ir:.2f}")

#Calculo do INSS
inss = salario_bruto * (0.08)
print(f"O valor pago ao INSS é de R${inss:.2f}")

#Calculo do sindicato 
sindicato = salario_bruto * (0.05)
print(f"O valor pago ao sindicato é de R${sindicato:.2f}")

#Salário líquido
salario_liquido = (salario_bruto - ir - inss - sindicato)
print(f"O valor do seu salário líquido é de R${salario_liquido:.2f}")

