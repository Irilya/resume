def comp_count():
    count = int(input("Введите количество комьютеров (целое число): "))
    if count % 10 == 1:
        print(f"{count} компьютер")
    elif count % 10 == 2 or count % 10 == 3 or count % 10 == 4:
        print(f"{count} компьютера")
    else:
        print(f"{count} компьютеров")


comp_count()
