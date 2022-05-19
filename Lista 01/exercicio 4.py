'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''
tf = float(input('Informe a temperatura em ºF: '))

tc = 5 * ((tf-32) / 9)

temperatura = 'A temperatura de {}ºF corresponde a {}ºC!'
print(temperatura.format(tf, tc))