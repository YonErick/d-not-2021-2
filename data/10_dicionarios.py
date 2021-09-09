# Dicionário é uma estrutura da linhagem python 
# capaz de armazenar multiplos valores em uma única
# variavel, por meio de pares de chave-valor

pessoa = {
    # "Nome" é a chave
    # "Fulano de PlayerTalz" é o valor 
    "Nome": "Fulano de PlayerTalz", 
    "Sexo": "M",
    "Idade": 39,
    "Peso": 76,
    "Altura": 1.82
}

# Calculando o IMC (Indice de Massa Corporal)
imc = pessoa["Peso"] / (pessoa["Altura"] ** 2)
print(f"O IMC de {pessoa['Nome']} é {imc}.")


forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     #Retangulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"     #Triangulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     #Elipse
}

forma4 = {
    "base": 10,
    "altura": 5,
    "tipo": "W"     #Tipo não reconhecido
}

forma5 = {
    "legume": "batata",
    "fruta": "abacate",
    "tipo": "T"    
}

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R":   # Retângulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T": # Triangulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E": #Elipse
        return forma["base"] / 2 * forma["altura"] / 2 * pi
    else:
        # Gera um erro
        raise Exception("Tipo de forma não reconhecido.")
    
print(f"Área de um retângulo de 7.5x12: {calcular_area(forma1)}")
print(f"Área de um triangulo de 6x2.5: {calcular_area(forma2)}")
print(f"Área de uma elipse de 5x3: {calcular_area(forma3)}")
#print(f"Área de uma forma desconhecida de 10x5: {calcular_area(forma4)}")
print(f"Área de uma forma desconhecida de ?x?: {calcular_area(forma5)}")

