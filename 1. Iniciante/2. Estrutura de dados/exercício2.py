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
    
    
    def remover(self, key):
        atual = self.head
        prev = None

        while atual and atual.data != key:
            prev = atual
            atual = atual.next

        if not atual:
            print("Elemento não encontrado.")
            return
        
        if prev:
            prev.next = atual.next
        else:
            self.head = atual.next
        
        print(f"Elemento {key} removido.")
    

    def mostrarLista(self):
        atual = self.head   # começa com a cabeça atual da lista
        while atual:  # percorre a lista
            print(atual.data, end=" -> ")   # imprime o valor do nó
            atual = atual.next
        print("None")   # indica o fim da lista


os.system('cls')
# Demonstração
ll = LinkedList()
ll.insercao("1")  # Insere "1" no início da lista
ll.insercao("2")  # Insere "2" no início da lista
ll.mostrarLista()  # 2 -> 1 -> None
ll.remover("1")  # Remove o elemento "1"
ll.mostrarLista()  # 2 -> None
ll.remover("3")  # Tenta remover um elemento que não está na lista

