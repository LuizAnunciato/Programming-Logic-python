"Exercício 6 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês"

salario_hora = float(input("Informe quanto você ganha por hora em (R$): "))
horas_trabalhadas = int(input("Informe o número de horas trabalhadas no mês: "))
salario_total = (salario_hora * horas_trabalhadas)

print(f"Seu salário total nesse mês corresponde a: {salario_total}")
