# Escreva um programa que leia uma lista de números 
# e calcule a soma total desses números.

import os
from random import randint


def gerarNumerosLista(quantidade):
  listaNumeros = []
  for i in range(0, quantidade):
   novoNumero = randint(0, 1000)
   print(f'{i+1}° valor da lista: ', novoNumero)
   listaNumeros.append(novoNumero)
  return listaNumeros


def tamanhoDaLista():
  quantidade = int(input('Quantos número terá a lista: '))
  return quantidade


def somarLista(lista):
  somaFinal = 0
  for elemento in lista: # 'lista' é a coleção dos itens que estamos percorrendo e 'elemento' é a variável temporária do elemento do loop atual
    somaFinal += elemento
  return somaFinal


os.system('cls')
quantidade = tamanhoDaLista()
listaFinal = gerarNumerosLista(quantidade)
print(listaFinal)
somaLista = somarLista(listaFinal)
print('Soma da lista: ', somaLista)
