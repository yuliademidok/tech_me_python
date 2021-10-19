"""2
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""


def unique_nums(arr: list):
    for elem in arr:
        if arr.count(elem) == 1:
            yield elem

    return None


some_arr = [2, 5, 6, 7, 42, 5, 6, 2, 0, 8, 8, 4, 3, 4]
for i in unique_nums(some_arr):
    print(i)