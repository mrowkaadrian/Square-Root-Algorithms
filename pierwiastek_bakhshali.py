import math


def estimate(number):
    d = len(str(number))
    if d % 2 == 1:
        n = (d - 1)/2
        estimation = 2 * 10**n
    else:
        n = (d - 2)/2
        estimation = 6 * 10**n
    print("Estimation: " + str(estimation))
    return estimation


def get_relative_error(estimated, real):
    result = str(round((abs(estimated - real) / real) * 100, 5))
    return result + " %"


def my_sqrt(number):
    estimation = estimate(number)
    d = number - estimation**2
    p = d/(2 * estimation)
    a = estimation + p
    my_result = a - p**2/(2*a)
    real_result = math.sqrt(number)
    to_return = (my_result, real_result, get_relative_error(my_result, real_result))
    print(to_return)
    return to_return


my_sqrt(74523635432)
