print('Ola, mundo!')
nome = input('Qual seu nome? ')
print(f'Olá, {nome}!')
idade = int(input('Informe a sua idade: '))
if idade >= 18:
    print('Você ja pode beber!')
    print('Você ja pode tirar habilitação!')
else:
    print('Você não pode beber!')
    print('Você não pode tirar habilitação!')