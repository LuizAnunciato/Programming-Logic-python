"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de
        quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

lado_a = int(input("Digite o valor do lado A: "))
lado_b = int(input("Digite o valor do lado B: "))
lado_c = int(input("Digite o valor do lado C: "))


#Condição de verificação dos triângulos
if (lado_a + lado_b) == lado_c:
    print("Esses elementos formam um triângulo")
elif (lado_a + lado_c == lado_b):
    print("Esses elementos formam um triângulo")
elif (lado_b + lado_a == lado_c):
    print("Esses elementos formam um triângulo")
elif (lado_b + lado_c == lado_a):
    print("Esses elementos formam um triângulo")
elif (lado_c + lado_a == lado_b):
    print("Esses elementos formam um triângulo")
elif (lado_c + lado_b == lado_a):
    print("Esses elementos formam um triângulo")
else:
    print("Esses elementos não formam um triângulo")

print()

tipo_triangulo = ''

#Tipagem dos triângulos: Equilátero
tipo_triangulo_equilatero = (
    lado_a + lado_b == lado_c and
    lado_a + lado_c == lado_b and
    lado_b + lado_a == lado_c and
    lado_b + lado_c == lado_a and
    lado_c + lado_a == lado_b and
    lado_c + lado_b == lado_a
)

#Tipagem dos triângulos: Isósceles:
tipo_triangulo_isosceles = (
    lado_a == lado_b and 
    lado_b == lado_c and
    lado_c == lado_a
)

#Tipagem dos triângulos: Escaleno
tipo_triangulo_escaleno = (
    lado_a != lado_b != lado_c 
)

if tipo_triangulo == tipo_triangulo_equilatero:
    print("Esse triângulo é do tipo Equilátero")
elif tipo_triangulo == tipo_triangulo_isosceles:
    print("Esse triângulo é do tipo Isósceles")
else:
    print("Esse triângulo é do tipo Escaleno")
