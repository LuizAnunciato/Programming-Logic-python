"""
Exercício 58 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
numeros = []

conjunto_numeros = int(input("Digite um conjunto de números (0 para encerrar): "))

if conjunto_numeros > 0 and conjunto_numeros <= 1000:
    if conjunto_numeros != 0:
        numeros.append(conjunto_numeros)

    while True:
        conjunto_numeros = int(input("Digite um novo número para o conjunto (0 para encerrar): "))
        if conjunto_numeros == 0:
            break  
        numeros.append(conjunto_numeros)


    if numeros == []:
        print("Não possui nenhum número no conjunto")   
    else:  
        menor_valor = numeros[0]
        maior_valor = numeros[0]

        for i in numeros:
            if i < menor_valor:
                menor_valor = i
            if i > maior_valor:
                maior_valor = i

        soma = sum(numeros)

        print(f"Números inseridos: {numeros}")        
        print(f"O menor número do conjunto é {menor_valor}")
        print(f"O maior número do conjunto é {maior_valor}")
        print(f"A soma dos números do conjunto é {soma}")
else:
    print("Conjunto de números excedeu o valor limite de 1000.")
