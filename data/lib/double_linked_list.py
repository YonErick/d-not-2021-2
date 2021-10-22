"""
    Classe que representa cada unidade (elemento) da lista encadeada
    É dividido em três partes:
    1) O ponteiro para o nodo anterior da sequência (prev)
    2) Onde fica armazenada a informação relevante para o usuário (data)
    3) O ponteiro para o próximo nodo da sequência (next)
"""
class Node:
    def _init_(self, val):
        self.prev = None    # Ponteiro para o nodo anterior (None = nenhum)
        self.data = val     # Armazena a informação do usuário
        self.next = None    # Ponteiro para o próximo nodo (None = nenhum)

"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    - A lista encadeada é uma estrutura de dados formada por unidades
      de informação chamadas nodos ou nós.
    - Cada nodo da lista encadeada tem três partes: uma, que armazena a
      informação; a segunda, que guarda o endereço do nodo anterior; e a
      terceira, que guarda o endereço para o nodo seguinte da sequência
    - A qualquer momento, temos um conhecimento apenas limitado de onde
      se encontram todos os nodos da lista. Sabemos apenas onde está o
      primeiro e o último nodo da sequência. Os nodos intermediários precisam
      ser encontrados partindo-se do primeiro OU do último nodo e percorrendo
      a sequência
"""
class DoublyLinkedList:

    """
        Construtor da classe
    """
    def _init_(self):
        self.__head = None  # (cabeça) Aponta para o início da lista
        self.__tail = None  # (cauda) Aponta para o fim da lista
        self.__count = 0    # Contador de nodos

    """
        Método que informa se a lista está ou não vazia
    """
    def is_empty(self):
        return self.__count == 0

    """
        Método para inserção de um novo nodo na lista
    """

    def __find_node(self, pos):
        if pos < self.__count // 2:
            node = self.__head
            for i in range(1, pos): node = node.next 
        else: 
            node = self.__tail
            for i in range(self.__count - 2, pos, -1): node = node.prev

        return node 

    def insert(self, pos, val):

        inserted = Node(val)

        # 1º caso: lista vazia
        # O nodo criado será, ao mesmo tempo, o primeiro e o último
        if(self.is_empty()):
            self.__head = inserted
            self.__tail = inserted

        # 2º caso: inserção na posição inicial
        elif pos == 0:
            inserted.next = self.__head     # Aponta para o seguinte
            self.__head.prev = inserted     # Aponta para o anterior
            self.__head = inserted          # Ajusta o início da lista

        # 3º caso: inserção na posição final
        elif pos >= self.__count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        else:
            node_pos = self.__findNode(pos)
            before = node_pos.prev
            after = node_pos.next

            before.next = inserted
            inserted.prev = before
            inserted.next = node_pos
            node_pos.prev = inserted

        self.__count += 1

    """
        Método que exibe a lista como uma string (para fins de depuração)
    """
    def to_str(self):
        string = ""
        Node = self.__head
        for i in range(0, self.__count):
            if string != "": string += ", "
            string += f"(pos: {i}, data: {node.data})"
            node = node.next
        return "[ " + string + f" ], count: {self.__count}"

###########################################################################

lista = DoublyLinkedList()
print(lista.to_str())

# Inserção em lista vazia
lista.insert(0, 'Fusca')
print(lista.to_str())

# Inserção no início da lista
lista.insert(0, 'Chevette')
print(lista.to_str())

# Inserção no final da lista
lista.insert(3, 'Maverick')
print(lista.to_str())

# Inserção no final da lista (2)
lista.insert(4, 'Opala')
print(lista.to_str())

lista.insert(5, 'Del Rey')
print(lista.to_str())

lista.insert(6, 'Gol')
print(lista.to_str())

lista.insert(7, 'Corcel')
print(lista.to_str())

# print(lista.find_node(0))
# print(lista.find_node(1))
# print(lista.find_node(2))
# print(lista.find_node(3))