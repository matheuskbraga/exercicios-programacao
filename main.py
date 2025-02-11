import os 

# 1 - Faça um algoritmo que leia os valores de A, B, C 
# e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.


def numero_de_valores(quantidade):
  lista = []
  for i in range(1, quantidade + 1): # range fala: conte do 1 até a 'quantidade' + 1
    valor = input(f'Digite o {i}° valor: ') # 'i' é o contador/índice
    lista.append(valor) # append() adiciona o valor na lista
  return lista


def definirTamanhoLista():
  quantidade_de_valores = int(input('Digite o tamanho da lista: '))
  return quantidade_de_valores


os.system('cls')
tamanhoLista = definirTamanhoLista()
listaFinal = numero_de_valores(tamanhoLista)
print(listaFinal)