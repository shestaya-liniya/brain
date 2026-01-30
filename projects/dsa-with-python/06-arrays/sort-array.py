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

def shift_arr_left(arr):
    arr_len = len(arr)
    last_element = arr[arr_len - 1]

    for k in range(arr_len - 1):
        arr[k], arr[k+1] = arr[k+1], arr[k]

    arr[0] = last_element

    return arr

def shift_arr_right(arr):
    arr_len = len(arr)
    last_element = arr[arr_len - 1]

    for k in range(arr_len - 2, 1, -1):
        arr[k - 1], arr[k] = arr[k], arr[k - 1]

    arr[0] = last_element

    return arr

def sort_array_v2(arr):
    """
    Use only one array
    """

print(arr)
print(shift_arr_left(arr))
print(shift_arr_right(arr))
