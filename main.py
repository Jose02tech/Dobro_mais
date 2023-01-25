from math import sqrt
num = float(input('Digite um número: '))
print('Dobro = \033[4;32;41m{}\033[m\nTriplo = \033[4;33;42m{}\033[m\nRaíz Quadra = \033[4;34;43m{:.2f}\033[m'.format(num * 2, num * 3, sqrt(num)))
