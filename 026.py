"""
Exercício 26 -
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""

salario_atual = float(input("Digite seu salário: "))

if salario_atual < 280.00:
    percentual_aumento = 0.20
    print(f"Seu percentual de aumento aplicado é {percentual_aumento * 100:.2f}%")
elif salario_atual >= 280.00 and salario_atual < 700.00:
    percentual_aumento = 0.15
    print(f"Seu percentual de aumento aplicado é {percentual_aumento * 100:.2f}%")
elif salario_atual >= 700.00 and salario_atual < 1500.00:
    percentual_aumento = 0.10
    print(f"Seu percentual de aumento aplicado é {percentual_aumento * 100:.2f}%")
else:
    percentual_aumento = 0.05
    print(f"Seu percentual de aumento aplicado é {percentual_aumento * 100:.2f}%")

# Salário antes do reajuste
print(f"Salário antes do reajuste: R${salario_atual:.2f}")

# Valor do aumento
valor_aumento = salario_atual * percentual_aumento
print(f"O valor do seu aumento é de R${valor_aumento:.2f}")

# Salário reajustado
salario_reajustado = salario_atual + valor_aumento
print(f"Salário reajustado: R${salario_reajustado:.2f}")
