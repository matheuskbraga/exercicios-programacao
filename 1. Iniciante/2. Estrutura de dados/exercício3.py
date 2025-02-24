# faça uma pilha em python

import os

class Pilha:


  def __init__(self):
    self.itens = []


  def pilhaVazia(self):
    return len(self.itens) == 0
  

  def empilharPilha(self, item):
    self.itens.append(item)
  

  def desempilhar(self):
    if not self.pilhaVazia():
      return self.itens.pop()
    else:
      return "A pilha está vazia"
  

  def topoPilha(self):
    if not self.pilhaVazia():
      return self.itens[-1]
    else:
      return "A pilha está vazia"
    

  def tamanhoPilha(self):
    return len(self.itens)


os.system('cls')
pilha = Pilha()
pilha.empilharPilha(15)
pilha.empilharPilha(25)
pilha.empilharPilha(34)
pilha.empilharPilha(413)
print("Topo da pilha:", pilha.topoPilha())
print("Tamanho da pilha:", pilha.tamanhoPilha())
print("Desempilhando:", pilha.desempilhar())
print("Topo da pilha após desempilhar:", pilha.topoPilha())
print("Tamanho da pilha após desempilhar:", pilha.tamanhoPilha())