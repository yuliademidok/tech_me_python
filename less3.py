# user_template = (
#     ("name", str),
#     ("surname", str),
#     ("age", int)
# )
#
# user = {}
#
# input_data = input(user_template[0][0])
# if not isinstance(input_data, user_template[0][1]):
#     print("ERROR", user_template[0][1])
# user[user_template[0][0]] = input_data
#
# input_data = input(user_template[1][0])
# if not isinstance(input_data, user_template[1][1]):
#     print("ERROR", user_template[1][1])
# user[user_template[1][0]] = input_data
#
# input_data = input(user_template[2][0])
# if not input_data.isdigit():
#     print("ERROR", user_template[2][1])
# user[user_template[2][0]] = user_template[2][1](input_data)
#
# print(user)





# num = 154
#
# result = ("BUZZ" * (not (num % 3)) + "FUZZ" * (not (num % 5))) or num
# print(result)





# user_template = (
#     {
#         "title": "name",
#         "type": str,
#         "error": "Ошибка ввода имени",
#         "input_string": "Представтесь"
#     },
#     {
#         "title": "age",
#         "type": int,
#         "error": "Ошибка ввода возраста",
#         "input_string": "Сколько вам лет"
#     }
# )
# user = {}
#
# template_count = len(user_template)
# n = 0
# while n < template_count:
#     field_template = user_template[n]
#     user_input = input(f'{field_template["input_string"]}\n>>>')
#     error = False
#     if field_template["type"] is not int:
#         pass
#     elif field_template["type"] is int and not user_input.isdigit():
#         error = not error
#     if error:
#         print(field_template["error"])
#         continue
#
#     user[field_template["title"]] = user_input
#     n += 1
#
# print(user)



user_input = "1 2 34 4"
arr = user_input.split(" ")
int_arr = 0
for i in arr:
    int_arr += int(i)
print(int_arr)
