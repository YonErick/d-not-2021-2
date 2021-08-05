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