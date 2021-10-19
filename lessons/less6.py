# a = 5
# b = 0
#
# try:
#     result = a / b
# except ZeroDivisionError:
#     print("ZDE")
# except (KeyError, IndexError):
#     print("KeyE")
# finally:
#     print("fin")


def some(a, b, c):
    h = []
    result = None

    try:
        if c:
            result = a / b
        else:
            result = h[a]

        # return "hello!!!"

    except ZeroDivisionError:
        print("ZDE")
    except (KeyError, IndexError):
        print("KeyE")
    finally:
        print("fin")

    return result


a = some(1, 2, 0)
print(a)
