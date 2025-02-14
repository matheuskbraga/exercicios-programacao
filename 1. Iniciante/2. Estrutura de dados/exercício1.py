# Crie um array que armazene 10 números inteiros. Implemente as operações básicas de inserção, remoção e busca nesse array.


import os


def armazenarNumeros():
  lista = []
  for valor in range(3):
    novoValor = int(input(f'Digite o {valor+1}° valor: '))
    lista.append(novoValor)
  print('Lista:', lista)
  return lista


def menuPrincipal():
  respostasValidas = 1,2,3
  loop = True
  while loop:
    print('Selecione uma das seguintes funções:')
    print('[1] Inserir')
    print('[2] Remover')
    print('[3] Buscar')
    resposta = int(input('Resposta: '))
    if resposta in respostasValidas:
      loop = False
    else:
      continue
  return resposta


def operacaoDesejada(escolha, lista):
  # Inserção
  if escolha == 1:
    novoValor = int(input('Digite o valor a ser inserido: '))
    lista.append(novoValor)
    print(f'Valor inserido: {novoValor}')
    print(lista)

  # Remoção
  elif escolha == 2:
    novoValor = int(input('Digite o valor a ser deletado: '))
    if novoValor in lista:
      lista.remove(novoValor)
      print(f'Valor removido: {novoValor}')
      print(lista)

  # Busca  
  elif escolha == 3: 
    novoValor = int(input('Digite o valor a ser buscado: '))
    if novoValor in lista:
      posicao = lista.index(novoValor)
      print(f'Este valor está na posição: {posicao+1}° posição')
      print(lista)


os.system('cls')
lista = armazenarNumeros()
while True:
  decisao = menuPrincipal()
  operacaoDesejada(decisao, lista)