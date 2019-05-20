import time


def bd_square(bd):
    comma_existed = False
    if ',' in bd:
        from_end = 2*(len(bd) - (bd.index(',') + 1))
        bd.remove(',')
        comma_existed = True

    it = len(bd)
    it2 = 0
    numbers_to_sum = []
    while it > 0:
        it = it - 1
        numbers_to_sum.append(bd.copy())
        bd_multiply(numbers_to_sum[it2], bd[it])
    # -- tutaj nastepuje dodanie zer w tablicy po wyniku, aby uzyskac przesuniecie
        for i in range(it2):
            numbers_to_sum[it2].append('0')
    # --
        it2 = it2 + 1

    square_result = bd_sum_arrays(numbers_to_sum)

    if comma_existed:
        square_result.insert(-from_end, ',')

    return square_result


def bd_sum_arrays(aoa):     # aoa = array of arrays
    sum_result = []
    for number in aoa:
        sum_result = bd_add(sum_result, number)
    return sum_result


def check_result(sq_result, expected):
    if '' in sq_result:
        sq_result.remove('')
    return bd_subtract(sq_result, expected)


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
        if bd[it] == ',':
            continue
        new_digit = int((int(bd[it]) * int(number)) + rest)
        if new_digit > 9:
            rest = int(new_digit / 10)
            new_digit = new_digit - rest * 10
        else:
            rest = 0
        bd[it] = new_digit
    if rest != 0:
        bd.insert(0, rest)


def bd_add(bd1, bd2):
    commas_existed = False
    bds = bd_align(bd1, bd2)
    bd1 = bds[0]
    bd2 = bds[1]
    if ',' in bd1:
        if ',' in bd2:
            comma_index = bd1.index(',')
            bd1.remove(',')
            bd2.remove(',')
            commas_existed = True

    it = len(bd1)
    carry = 0
    while it > 0:
        it = it - 1
        if int(bd1[it]) + int(bd2[it]) + carry >= 10:
            bd1[it] = (int(bd1[it]) + int(bd2[it]) + carry) % 10
            carry = 1
        else:
            bd1[it] = int(bd1[it]) + int(bd2[it]) + carry
            carry = 0

    if commas_existed:
        bd1.insert(comma_index, ',')
        bd2.insert(comma_index, ',')

    if carry == 1:
        bd1.insert(0, '1')

    return bd1


def bd_align(bd1, bd2):
    commas_existed = False

    if ',' in bd1 and ',' not in bd2:
        bd2.append(',')

    if ',' not in bd1 and ',' in bd2:
        bd1.append(',')

    if ',' in bd1 and ',' in bd2:
        commas_existed = True
        comma_difference = bd1.index(',') - bd2.index(',')
        zeros_before = [0] * abs(comma_difference)
        if comma_difference > 0:
            bd2 = zeros_before + bd2
        if comma_difference < 0:
            bd1 = zeros_before + bd1

    len_difference = len(bd1) - len(bd2)
    zeros = [0] * abs(len_difference)
    if commas_existed:
        if len_difference > 0:
            bd2 = bd2 + zeros
        if len_difference < 0:
            bd1 = bd1 + zeros
    else:
        if len_difference > 0:
            bd2 = zeros + bd2
        if len_difference < 0:
            bd1 = zeros + bd1
    return [bd1, bd2]


def bd_subtract(big_decimal1, big_decimal2):
    bds = bd_align(big_decimal1, big_decimal2)
    bd1 = bds[0]
    bd2 = bds[1]
    sub_result = bd1.copy()

    it = len(bd1)

    borrow = 0
    while it > 0:
        it = it - 1
        if bd1[it] == ',' and bd2[it] == ',':
            continue
        if int(bd1[it]) < int(bd2[it]):
            sub_result[it] = int(bd1[it]) + 10 - int(bd2[it]) - borrow
            borrow = 1
        else:
            new_digit = int(bd1[it]) - int(bd2[it]) - borrow
            if new_digit < 0:
                new_digit = 9
                borrow = 1
                sub_result[it] = new_digit
                continue
            sub_result[it] = new_digit
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

    if result_arr.index(',') == len(result_arr) - 1:
        result_arr.remove(',')


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
    print(val, sep=' ', end='')

squared = bd_square(result)

print("       ")

for val in squared:
    print(val, sep=' ', end='')

print("\nPomyłka o:")
err = check_result(array, squared)

for val in err:
    print(val, sep=' ', end='')