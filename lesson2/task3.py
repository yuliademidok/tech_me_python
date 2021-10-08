"""
3 Даны 2 списка и список чисел, написать процедуру и распределить числа по спискам
числа четные должны попасть в список even, числа нечетные должны попасть в список odd
"""
numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

arr = (even, odd)

arr[numbers[0] % 2 == 0].append(numbers[0])
arr[numbers[1] % 2 == 0].append(numbers[1])
arr[numbers[2] % 2 == 0].append(numbers[2])
arr[numbers[3] % 2 == 0].append(numbers[3])
arr[numbers[4] % 2 == 0].append(numbers[4])
arr[numbers[5] % 2 == 0].append(numbers[5])
arr[numbers[6] % 2 == 0].append(numbers[6])
arr[numbers[7] % 2 == 0].append(numbers[7])
arr[numbers[8] % 2 == 0].append(numbers[8])
arr[numbers[9] % 2 == 0].append(numbers[9])
arr[numbers[10] % 2 == 0].append(numbers[10])

print(even)
print(odd)

