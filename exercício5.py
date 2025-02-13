# Crie um programa que converta uma temperatura de Celsius para Fahrenheit.

import os


def conversao(celcius):
  fahrenheit = (celcius * 9/5) + 32
  return fahrenheit


os.system('cls')
temperaturaCelsius = int(input('Digite a temperatura em gareus Celcius: '))
temperaturaFahrenheit = conversao(temperaturaCelsius)
print(f'A temperatura ficou {temperaturaFahrenheit}° Fahrenheit')
