class Deque:

    """
        ESTUTURA DE DADOS DEQUE
        - Deque = Double-Ended Queue (fila de duas pontas)
        - Deque é uma lista linear de acesso restrito, que permite apenas as operações
            de enfileiramento (insert_front/insert_back) e desenfileiramento
            (remove_front/remove_back), acontecendo em qualquer uma das extremidades da estrutura.
            - Como consequência, o deque NÃO SEGUE o princípio FIFO (First In, First Out - primeiro a entrar, primeiro a sair).
        - A principal aplicação dos deques são situações em que filas precisam aceitar
        a inserção de itens prioritários e a desistência do último item.
    """

    """
        Construtor da classe
    """
    def _init_(self):
        self.__data = []    # Inicializa uma lista privada vazia

    """
        Método para inserção no início do deque
    """
    def insert_front(self, val):
        self.__data.insert(0, val)

    """
        Método para inserção no final do deque
    """
    def insert_back(self, val):
        self.__data.append(val)

    """
        Método para remoção do início do deque
    """
    def remove_front(self):
        if self.is_empty(): return None
        return self.__data.pop(0)

    """
        Método para remoção do final do deque
    """
    def remove_back(self):
        if self.is_empty(): return None
        return self.__data.pop()

    """
        Método para consultar o início do deque (primeiro elemento), sem retirá-lo
    """
    def peek_front(self):
        if self.is_empty(): return None
        return self.__data[0]

    """
        Método para consultar o final do deque (último elemento), sem retirá-lo
    """
    def peek_back(self):
        if self.is_empty(): return None
        return self.__data[-1]

    """
        Método para verificar se a fila está vazia ou não
        Retorna True se vazia ou False caso contrário
    """
    def is_empty(self):
        return len(self.__data) == 0

    """
        Método que exibe a fila como uma string (para fins de depuração)
    """
    def to_str(self):
        string = ""
        for el in self.__data:
            if string != "": string += ", "
            string += str(el)
        return "[ " + string + " ]"

######################################################

deque = Deque()     # Cria um deque vazio
print(deque.to_str())

# Inserções "normais"
deque.insert_back("Tertuliano")
deque.insert_back("Castorina")
deque.insert_back("Astolfo")
deque.insert_back("Wesclerson")
deque.insert_back("Gilvanete")

print(deque.to_str())

# Inserções prioritárias
deque.insert_front("Hermóneges")
deque.insert_front("Querência")

print(deque.to_str())

# Remoções "normais"
atendido = deque.remove_front()
print(f"Atendido: {atendido}")
print(deque.to_str())

atendido = deque.remove_front()
print(f"Atendido: {atendido}")
print(deque.to_str())

# Desistências (remoção no final)
desistente = deque.remove_back()
print(f"Desistente: {desistente}")
print(deque.to_str())

desistente = deque.remove_back()
print(f"Desistente: {desistente}")
print(deque.to_str())

# Consultando as extremidades do deque
primeiro = deque.peek_front()
ultimo = deque.peek_back()
print(f"Primeiro: {primeiro}, último: {ultimo}")
print(deque.to_str())