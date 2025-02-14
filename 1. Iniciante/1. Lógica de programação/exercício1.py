import os 

# 1 - Faça um algoritmo que leia os valores de A, B, C 
# e em seguida imprima na tela a soma entre A e B e mostre se a soma é menor que C.


os.system('cls')
valor_A = int(input('Digite o valor de A: '))
valor_B = int(input('Digite o valor de B: '))
valor_C = int(input('Digite o valor de C: '))

soma = valor_A + valor_B
print(f'Valor da soma: {soma}')

if(soma < valor_C):
  print('A soma é menor que C.')
else:
  print('A soma é igual ou maior que C')