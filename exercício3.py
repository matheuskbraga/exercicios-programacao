# Crie um programa que leia um número 
# e verifique se ele é par ou ímpar.


import os
from random import randint


def leitor():
  numero = randint(1, 100)
  print('O número é:', numero)
  return numero


def verificador(numero):
  if numero % 2 == 0:
    print('Número: Par')
  else:
   print('Número: Ímpar')


os.system('cls')
numero = leitor()
verificador(numero)
