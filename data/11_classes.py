# Classe é uma estrutura que representa conjuntamente 
# dados e algoritimos. Uma classe é como uma "forma de bolo"
# com o qual podemos criar diferentes "bolos" (objetos).
# Cada "bolo" (objeto) pode ser feito com seus próprios
# Ingredientes (dados) e modos de fazer (algoritimos), mas
# terão sempre o formato determinado pela "forma" (classe).

class FormaGeometrica():

    # Dados
    base = 0
    altura = 0
    tipo = "R"  # Retângulo

    # Algoritimos
    # São representados por funções que, quando se encontram
    # dentro de uma classe, ganham o nome de MÉTODOS

    # Este método é executado quando um objeto é criado a partir
    # de uma classe
    
    def __init__(self, base = 0, altura = 0, tipo = "R"):
        # Recebe os valores passados ao construtor e os armazena 
        # dentro dos atributos

        if base <= 0:
            raise Exception("A base deve ser maior que zero")
        elif altura <= 0:
            raise Exception("A altura deve ser maior que zero")
        elif tipo not in ["R", "T", "E"]:
            raise Exception("O tipo deve ser R, T ou E")


        self.base = base
        self.altura = altura
        self.tipo = tipo

###################################################################

# Criando objetos a partir da classe

retangulo1 = FormaGeometrica( 15, 10, "R")
triangulo1 = FormaGeometrica( 6, 9, "T")

print(f"[retangulo1] base: {retangulo1.base}, altura: {retangulo1.altura}, tipo: {retangulo1.tipo} ")
print(f"[triangulo1] base: {triangulo1.base}, altura: {triangulo1.altura}, tipo: {triangulo1.tipo} ")