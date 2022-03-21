import random
from random import choice

first = random.choice(range(2, 10))
second = random.choice(range(2, 10))
ar = choice(["+", "-", "*"])

if ar == '+':
    print(str(first) + ' + ' + str(second))
    res = first + second
elif ar == '-':
    print(str(first) + ' - ' + str(second))
    res = first - second
elif ar == '*':
    print(str(first) + ' * ' + str(second))
    res = first * second

answer = int(input(">"))

if res == answer:
    print('Right!')
else:
    print('Wrong!')
