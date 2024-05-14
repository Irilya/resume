def multiplication_table():
    number = int(input('Введите число: '))
    num = 1
    print(f'    ', end='')
    for i in range(1, number+1):
        print(f'{i}', end='  ')
    print()
    while num <= number:
        print(num, end='   ')
        for i in range(1, number+1):
            print(f'{num * i}', end='  ')
        num += 1
        print()


multiplication_table()
