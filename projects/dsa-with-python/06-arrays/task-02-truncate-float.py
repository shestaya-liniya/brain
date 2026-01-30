'''
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается.
Каждый год сумма вклада становится больше. Надо определить, через сколько лет вклад составит не менее y рублей.

Формат входных данных
Три натуральных числа: x, p, y.

Формат выходных данных
Число лет, через сколько лет вклад составит не менее y рублей.
'''

input_string = input()

def split(str, n, sep = " ", should_convert_to_int = True):
    arr = [0] * n
    sub_str = ""

    arr_i = 0

    for k in str:
        if k == sep:
            if sub_str != "":
                arr[arr_i] = sub_str
                arr_i += 1
            sub_str = ""

        else:
            sub_str += k

    # handling last substring as it can not have a separator after
    arr[arr_i] = sub_str

    if should_convert_to_int:
        for k in range(len(arr)):
            arr[k] = int(arr[k])
            
    return arr

def truncate_float(num: float, max_fraction_digits: int) -> float:
    float_str = str(num)
    ints_str = ""
    fraction_digits_str = ""
    does_reached_fraction_digits = False

    for char in float_str:
        if char == ".":
            does_reached_fraction_digits = True
            # skip point
            continue

        if does_reached_fraction_digits:
            fraction_digits_str += char
        else:
            ints_str += char

    if len(fraction_digits_str) > max_fraction_digits:
        tmp = ""

        for i in range(max_fraction_digits):
            tmp += fraction_digits_str[i]

        fraction_digits_str = tmp

    return float(ints_str + "." + fraction_digits_str)

nums = split(input_string, 3)
x = nums[0]
p = nums[1]
y = nums[2]

count = 0
while x < y:
    one_percent = x / 100
    x += truncate_float(one_percent * p, 2)

    count += 1

print(count)