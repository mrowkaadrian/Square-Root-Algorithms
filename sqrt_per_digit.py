import datetime
import time


def fill_array(array_name, filename):
    file = open(filename, "r")
    while True:
        value = file.read(1)
        array_name.append(value)
        if not value:
            break
    file.close()


def bd_multiply(bd, number):         # mnozy wielka liczbe przez cyfre z zakresu od 1 do 9
    it = len(bd)       # iterator
    rest = 0
    while it > 0:
        it = it - 1
        new_digit = int((bd[it] * number) + rest)
        if new_digit > 9:
            rest = int(new_digit / 10)
            new_digit = new_digit - rest * 10
        else:
            rest = 0
        bd[it] = new_digit
    if rest != 0:
        bd.insert(0, rest)


def bd_subtract(big_decimal1, big_decimal2):
    sub_result = big_decimal1.copy()
    bd1 = big_decimal1.copy()
    bd2 = big_decimal2.copy()
    while len(bd1) != len(bd2):
        if len(bd1) > len(bd2):
            bd2.insert(0, '0')
        if len(bd1) < len(bd2):
            bd1.insert(0, '0')

    it1 = len(bd1)
    it2 = len(bd2)
    if it1 < it2:
        print("BLAD: Liczba ujemna")
        return 0
    borrow = 0
    while it2 > 0:
        it1 = it1 - 1
        it2 = it2 - 1
        if int(bd1[it1]) < int(bd2[it2]):
            sub_result[it1] = int(bd1[it1]) + 10 - int(bd2[it2]) - borrow
            borrow = 1
        else:
            new_digit = int(bd1[it1]) - int(bd2[it2]) - borrow
            if new_digit < 0:
                new_digit = 9
                borrow = 1
                sub_result[it1] = new_digit
                continue
            sub_result[it1] = new_digit
            borrow = 0

    return sub_result


def bd_get_y(p, x):
    y = p.copy()
    bd_multiply(y, 2)
    y.append(x)
    bd_multiply(y, x)
    return y


def bd_get_c(r, dig1, dig2):
    c = r.copy()
    if c == [0] or c == ['0']:
        c = []
    c.append(dig1)
    c.append(dig2)
    return c


def bd_is_left_greater_or_equal(big_decimal1, big_decimal2):
    bd1 = big_decimal1.copy()
    bd2 = big_decimal2.copy()
    while len(bd1) != len(bd2):
        if len(bd1) > len(bd2):
            bd2.insert(0, '0')
        if len(bd1) < len(bd2):
            bd1.insert(0, '0')

    val1 = 0
    val2 = 0
    it = 0
    while val1 == val2:
        if it == len(bd1):
            return True
        val1 = int(bd1[it])
        val2 = int(bd2[it])
        it = it + 1
    if val1 < val2:
        return False
    else:
        return True


def bd_num_to_arr(num):

    arr = []
    while num > 0:
        digit = num % 10
        num = num / 10
        arr.append(digit)
    arr.reverse()
    return arr


def bd_is_not_zero(num):
    for val in num:
        if val != '0' and val != 0:
            return True

    return False


def my_sqrt(big_decimal, result_arr):

    if (len(big_decimal)-1) % 2 == 1:    # jesli dlugosc liczby jest nieparzysta, nalezy dodac 0 na poczatku
        big_decimal.insert(0, "0")
    counter = 1     # licznik, aby wstawic przecinek
    r = [0]           # reszta
    p = [0]

    while counter < len(big_decimal):
        c = bd_get_c(r, big_decimal[counter - 1], big_decimal[counter])
        counter = counter + 2       # przesuniecie licznika o 2 w prawo
        y = [0]
        x = -1

        while bd_is_left_greater_or_equal(c, y):
            x = x+1
            y = bd_get_y(p, x)

        x = x-1
        y = bd_get_y(p, x)
        result_arr.append(x)
        p.append(x)
        r = bd_subtract(c, y)

    result_arr.append(",")
    #print("\nr = " + str(r))

    # obliczanie wartosci po przecinku:

    for i in range(50):
        if bd_is_not_zero(r):
            c = bd_get_c(r, '0', '0')
            y = [0]
            x = -1

            while bd_is_left_greater_or_equal(c, y):
                x = x + 1
                y = bd_get_y(p, x)

            x = x - 1
            y = bd_get_y(p, x)
            p.append(x)
            result_arr.append(x)
            r = bd_subtract(c, y)
        else:
            break


array = []
result = []

time_start = time.time()

fill_array(array, "data.txt")
for val in array:
    print(val, sep=' ', end='')
my_sqrt(array, result)

print("\nCzas:  " + str(time.time()-time_start) + "s")

print("Wynik:")
for val in result:
    print(val, sep=' ', end='', flush=True)
