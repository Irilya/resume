from math import gcd
from functools import reduce


def common_divisor():
    divisors_list = []
    number_list = input('Введите массив чисел: ')
    number_list = [int(x) for x in number_list[1:-1].split(', ')]
    divisor = reduce(gcd, number_list)
    for n in range(1, int(divisor) + 1):
        if int(divisor) % n == 0:
            divisors_list.append(n)

    print(divisors_list)


common_divisor()
