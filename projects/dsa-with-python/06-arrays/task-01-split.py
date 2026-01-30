"""
Даны координаты точки и радиус круга с центром в начале координат. Определить, принадлежит ли данная точка кругу. 
Напомним, что круг – это часть плоскости, состоящая из всех точек окружности и всех точек, лежащих внутри окружности.

Формат входных данных
Три целых числа на одной строке: координата точки по оси x, координата точки по оси y, радиус круга r (r > 0).

Формат выходных данных
Вывести "YES" без кавычек, если точка принадлежит кругу, "NO" без кавычек в противном случае.
"""

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

    # handling last subsring as it can not have a separator after
    arr[arr_i] = sub_str

    if should_convert_to_int:
        for k in range(len(arr)):
            arr[k] = int(arr[k])
            
    return arr

nums = split(input_string, 3)

x = nums[0]
y = nums[1]
r = nums[2]

is_x_overflow = x > r or -x < -r
is_y_overflow = y > r or -y < -r
is_diagonal_overflow = (x**2 + y**2) ** 0.5 > r

if is_x_overflow or is_y_overflow or is_diagonal_overflow:
    print("NO")
else:
    print("YES")