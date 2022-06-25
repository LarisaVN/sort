# преобразование строк в число с фильтром
def str_to_num(num):

    array = []
    for i in num:
        try:
            array.append(int(i))
        except Exception:
            try:
                array.append(float(i))
            except Exception:
                continue

    array.sort()
    return array


# искомое число
def location_num(array):
    if len(array) > 0:
        while 1:
            kbd = input("Введите число:" + '\n')
            try:
                value = float(kbd)
                break
            except Exception:
                continue

        mid = len(array) // 2
        low = 0
        high = len(array) - 1

        while array[mid] != value and low <= high:
            if value > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            if low == 0:
                print("Числа меньше заданного нет. Индекс числа, которое больше заданного =", low)
            else:
                if low == len(array):
                    print("Индекс числа, которое меньше заданного =", high, ".  Числа больше заданного нет")
                else:
                    print("Индекс числа, которое меньше заданного =", high, ".  Индекс числа, которое больше заданного =", low)

        else:
            if mid == 0:
                print("Числа меньше заданного нет. Индекс числа, которое равно заданному =", mid)
            else:
                if high == len(array):
                    print("Индекс числа, которое меньше заданного =", high, ".  Числа больше заданного нет")
                else:
                    print("Индекс числа, которое меньше заданного =", mid - 1, ".  Индекс числа, которое равно заданному =", mid)
        return 0
    else:
        return -1


numbers = input("Введите числа через пробел:" + '\n')
if len(numbers) > 0:
    print("Введенные числа: ", numbers)

    numbers_2 = numbers.split()
    result = str_to_num(numbers_2)

    lstlen = len(result)
    if lstlen > 0:
        print("Количество чисел: ", lstlen)
        print("Отсортированные по возрастанию числа: ", result)
        location_num(result)
    else:
        print("Мало чисел!"+ '\n')
else:
    print("Неправильный ввод!" + '\n')