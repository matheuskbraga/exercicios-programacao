# Escreva um algoritmo que encontre o maior de três números fornecidos pelo usuário.

import os


def valoresDoUsuario():
  lista = []
  for i in range(3):
    valor = int(input(f'Digite o {i+1}° número: '))
    lista.append(valor)
  return lista


def verificarMaiorNumero():
  lista = valoresDoUsuario()
  maiorNumero = max(lista)
  return maiorNumero
      

os.system('cls')
maiorNumero = verificarMaiorNumero()
print(f'O maior valor da lista é {maiorNumero}')