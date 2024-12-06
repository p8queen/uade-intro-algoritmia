import random

n = int(input('ingrese un numero menor a 10: '))
while n<1 or n>10:
	n = int(input('ingrese un numero menor a 10: '))
a = random.randint(1,10)
print(n, a)
print()
