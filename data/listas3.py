# Lista de strings
frutas = ["laranja", "maçã", "uva", "pêra", "mamão", "abacaxi", "amora"]

# Imprimindo apenas a fruta "uva"
print(frutas[2])

# Substituindo "pêra" por "melão"
frutas[3] = "melão"
print(frutas)

# Descobrindo quantos elementos há na lista

print(len(frutas))

print('------------------')

for fruta in frutas:
    print(fruta)

# Percorrendo e imprimindo cada elemento e sua posição

for i in range(len(frutas)):
    print(f"{frutas[i]} esta na posição {i}")

#percurso em ordem invertida
#1 argumento: len(frutas) -1: a lista precisa começar no ultimo elemento, que é determinado por len() -1
#2 argumento: -1, porque o limite final não entra e precisamos terminar em 0
#3 argumento: -1, porque a lista precisa ser decrescente
for j in range(len(frutas) -1, -1, -1):
    print(frutas[j])

print('------------------')

#ordenando o vetor em ordem alfabética
frutas.sort()
print(frutas)