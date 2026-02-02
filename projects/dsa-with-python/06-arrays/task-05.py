"""
Есть результаты работы студентов в семестре. Студентов выводить в порядке суммы их баллов. Требутеся вывести отсортированные результаты работ для каждого студента.

Данные вводятся как: student_id value

student_id принимает значения от 0 до N. value от 1 до 10

Пример входных данных: 0 3 0 5 1 3 1 2

Тут представленны данные о двух студента: 0 и 1. Сумма балов студента 0 - 8. Студента 1 - 5. Значит, сначала должны быть напечатаны результаты 0 студента, затем 1.
Таким образом сначала надо вывести отсортированные результаты студента 0, затем студента 1:

5 3 3 2

Напомним, что у list в питоне есть встроенный метод sort и есть функция sorted. У них есть параметр key, который определяет по каким значениям будет сортироваться объект. Например код ниже будет сортировать лист по длинне его элементов. Так же есть параметр reverse.

a = ['###', '@', '??'] a.sort(key=lambda x: len(x)) a ['@', '??', '###'] a.sort(key=lambda x: len(x), reverse=True) ['###', '??', '@']

Что такое лямбда функция вы узнаете в дальнейшем (так же всегда есть сайт google). Для выполнения этого задания достаточно понять, на что надо заменить функцию len.

Формат входных данных
В первой строке N - количество студентов. Далее идет какое-то количество строк (не равное N) с результатами студентов в формате: student_id value. 0 <= student_id < N.
Значения разделены пробелом. Ввод заканчивается #.

Формат выходных данных
Вывести отсортированные результаты студентов в одну строку. Сначала печатаются результаты лучшего по сумме баллов студента, потом второго и так далее. Результаты в одну строку
"""

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

def sum_arr(arr):
    sum = 0

    for x in arr:
        sum += x

    return sum

def append_to_aray(arr, val):
    arr_len = len(arr)
    tmp = [0] * (arr_len + 1)

    for i in range(arr_len):
        tmp[i] = arr[i]

    tmp[arr_len] = val
    return tmp

students_count = int(input())
ids = [0] * students_count
grades = [[]] * students_count

while True:
    I = input()

    if I == "#":
        break

    parsed = split(I, 2)

    id = parsed[0]
    grade = parsed[1]

    grades[id] = list(append_to_aray(grades[id], grade))

grades.sort(key=lambda x: sum_arr(x), reverse=True)

result = ""
for x in grades:
    x.sort(reverse=True)
    for y in x:
        result += str(y) + " "

print(result)