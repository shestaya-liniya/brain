arr = [10, 3, 7, 2, 4, 8, 1, 3]

def sort_array(arr):
    sorted = []
    taken_indexes = []

    while len(arr) > 0:
        low = arr[0]
        low_i = 0

        for i in range(len(arr)):
            if arr[i] < low:
                low = arr[i]
                low_i = i

        taken_indexes += [low_i]
        sorted += [low]
        without_low = []

        for i in range(len(arr)):
            if i != low_i:
                without_low += [arr[i]]

        arr = list(without_low)
        
    return sorted

def shift_arr_right(arr):
    for i in range(len(arr) - 1, 0, -1):
        arr[i - 1], arr[i] = arr[i], arr[i - 1]

    return arr

def shift_arr_left(arr):
    for i in range(len(arr) - 1):
        arr[i + 1], arr[i] = arr[i], arr[i+1]

    return arr

def shift_arr_left_alt(arr):
    first_el = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[len(arr) - 1] = first_el

    return arr

def shift_arr_right_alt(arr):
    last_el = arr[len(arr) - 1]

    for i in range(len(arr) - 2, -1, -1):
        arr[i + 1] = arr[i]

    arr[0] = last_el

    return arr

def sort_array_v2(arr):
    """
    Use only one array
    """

print(arr)
print(shift_arr_left(list(arr)))
print(shift_arr_left_alt(list(arr)))
print(shift_arr_right(list(arr)))
print(shift_arr_right_alt(list(arr)))

