from math import pi 

# Funções é um trecho de codigo que tem um nome e pode
# receber informações externas para fazer seu trabalho.
# Opcionalmente, uma função pode tambem produzir um valor de resultado
# uma função é definida apenas uma vez e pode ser utilizada varias vezes
# evitando repetiçoes de codigo.
# Existem varias funções já providas pela linguagem, como, por exemplo,
# len(), range() e sort(), e podemos definir também nossas próprias funções.

def imc(peso, altura):
    return peso / altura ** 2 # peso / (altura)²

p = float(input('Informe o peso da pessoa:'))
a = float(input('Informe a altura da pessoa:'))

resultado = imc(p, a)

print(f"O IMC calculado é {resultado}.")

def area_forma(base, altura, forma = "R"):
    """
        função que calcula a area de uma das seguintes
        formas geometricas: retangulo, triangulo ou elipse
        parametro forma: 
        R = Retangulo
        T = Triangulo
        E = Elipse
    """
    area = 0
    if forma == "R":
        area = base * altura
    elif forma == "T":
        area = base * altura / 2
    elif forma == "E":
        area = (base / 2) * (altura / 2) * pi
    return area

print(f"Retangulo 7.5x11: {area_forma(7.5, 11, 'R')}")
print(f"Triangulo 8x12: {area_forma(8, 12, 'T')}")
print(f"Triangulo 15x15: {area_forma(15, 15, 'E')}")
print(f"Quadrado 9.5x9.5: {area_forma(9.5, 9.5)}")