def tag_deco(tag_name, class_string=""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            tag_class = f' class="{class_string}"' if class_string else ""
            return f"<{tag_name}{tag_class}>{result}</{tag_name}>"
        return wrapper
    return decorator


@tag_deco("html")
@tag_deco("body")
@tag_deco("div", "div_name")
@tag_deco("span", "some_span")
@tag_deco("p")
def user_name_counter(name, count):
    result = f"User: {name}, Count: {count}"
    return result


with open("hello.html", "w", encoding="UTF-8") as file:
    file.write(user_name_counter("Yulia", 22))

# print(user_name_counter("Yulia", 22))
