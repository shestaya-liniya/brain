'''
Шахматный ферзь может ходить на любое число клеток по горизонтали, по вертикали или по диагонали.
Даны две различные клетки шахматной доски, определите, может ли ферзь попасть c первой клетки на вторую одним ходом.
Для простоты можно не рассматривать случай, когда данные клетки совпадают.

Формат входных данных:
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

Формат выходных данных:
Программа должна вывести YES, если из первой клетки ходом ферзя можно попасть во вторую. B противном случае - NO.
'''

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x_index = x1
y_index = y1

while True:
    # first condition is the initial check by the vertical or horizontal
    # second conditoin is the iterable check by the diagional
    if (y1 == y2 or x1 == x2) or (x_index == x2 and y_index == y2):
        print("YES")
        break

    if x2 < x1:
        x_index -= 1
    else:
        x_index += 1

    if y2 < y1:
        y_index -= 1
    else:
        y_index += 1

    if x_index < 1 or x_index > 8 or y_index < 1 or y_index > 8:
        print("NO")
        break
    
