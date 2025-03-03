"""
"Exercício 25 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso
"""

print("Digite M-matutino ou V-Vespertino ou N- Noturno")
turno = input("Digite o turno em que você estuda: ").upper()

if turno == 'M':
    print("Bom dia")
elif turno == 'V':
    print("Boa tarde")
else:
    print("Boa noite")


