"""
Вводится последовательность, состоящая только из 0 и 1. Необходимо найти максимальное количество 1, идущих подряд (без 0 между ними).

Формат входных данных
В первой строке задается натуральное N<=10000 , длина массива, далее идут N чисел 0 или 1 -- элементы массива. Каждое число вводится с новой строки.

Формат выходных данных
Одно число — результат.
"""

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

max_sequence = 0
curr_sequence = 0

for x in A:
    if x == 1:
        curr_sequence += 1

        if curr_sequence > max_sequence:
            max_sequence = curr_sequence
    else:
        curr_sequence = 0

print(max_sequence)
