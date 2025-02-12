#Implemente um jogo de adivinhação onde o usuário deve adivinhar um número entre 1 e 10 que é gerado aleatoriamente pelo programa e tem 3 chances de adivinhar o valor.


import os
from random import randint


def gerarValor():
  valorEscolhido = randint(1,10)
  print('Valor sorteado:', valorEscolhido)
  return valorEscolhido


def usuarioChances(totalChances, valorSorteado):
  for chance in range(totalChances):
    resposta = int(input('Digite o número da sua resposta: '))
    if resposta == valorSorteado:
      print(f'Você acertou na {chance+1}° chance!')
      break
    else:
      print('Errou!')
    if chance+1 == 3:
      print('Suas chances acabaram. Tente novamente!')
      break


os.system('cls')
valorSorteado = gerarValor()
usuarioChances(3, valorSorteado)