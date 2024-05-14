def simple_numbers():
    simple_numbers_list = []
    min_number = input('Введите наименьшее число: ')
    max_number = input('Введите наибольшее число: ')
    count = 0

    for num in range(int(min_number), int(max_number)):
        for n in range(2, num//2 + 1):
            if num % n == 0:
                count += 1
        if count == 0:
            simple_numbers_list.append(num)
        count = 0

    print(simple_numbers_list)


simple_numbers()
