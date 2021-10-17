"""5
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ (например Q), выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_func(delimiter="Q"):
    result = 0

    def iter_func():
        numbers = input("Enter numbers\n>>>")
        num_arr = numbers.split()
        nonlocal result

        if delimiter in num_arr:
            result += sum(int(i) for i in num_arr[:num_arr.index(delimiter)])
            print(f"Result: {result}")
            return result

        result += sum(int(i) for i in num_arr)
        print(f"Result: {result}\n")

        return iter_func()

    iter_func()

    return result


my_func()
