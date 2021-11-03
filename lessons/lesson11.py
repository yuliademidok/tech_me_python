# def some(func):
#     counter = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal counter
#         counter += 1
#         print(func.__name__, counter)
#
#         return func(*args, **kwargs)
#
#     return wrapper


def func_log(file_name, data):
    with open(file_name, "a", encoding="UTF-8") as file:
        file.write(data)


def log_some(file_name):
    def decorator(func):
        counter = 0

        def wrapper(*args, **kwargs):
            nonlocal counter
            counter += 1
            func_log(file_name, counter)
            result = func(*args, **kwargs)

            return result
        return wrapper

    return decorator


@log_some("log.txt")
def my_func(a, b):
    return a + b


print(my_func('2', '3'))



# def some2(func, **kw):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kw, **kwargs)
#
#     return wrapper
#
#
# A = 2
# B = [2, 3, 56, 3, 456, 5]
# func = some2(my_func, b=A)
#
# results = []
# for i in B:
#     results.append(func(i))
#
# print(results)
