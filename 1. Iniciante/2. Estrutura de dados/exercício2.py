# Implemente uma lista ligada simples com operações básicas de inserção, remoção e busca.
import os


class Node:
    def __init__(self, data):
        self.data = data  # Armazena o dado do nó
        self.next = None  # Inicializa o próximo nó como None


class LinkedList:
    def __init__(self):
        self.head = None  # Inicializa a lista ligada com a cabeça (head) como None

    def insercao(self, data):
        novo_no = Node(data)  # Cria um novo nó do valor recebido
        novo_no.next = self.head  # Faz com que o nó aponte para a antiga cabeça da lista
        self.head = novo_no # A nova cabeça da lista é o novo nó criado nesta função
        

    def mostrarLista(self):
        atual = self.head   # começa com a cabeça atual da lista
        while atual:  # percorre a lista
            print(atual.data, end=" -> ") # imprime o valor do nó
            atual = atual.next
        print("None")


os.system('cls')

# Demonstração
ll = LinkedList()
ll.insercao("B")  # Insere "B" no início da lista
ll.insercao("A")  # Insere "A" no início da lista
ll.mostrarLista()  # A -> B -> None

