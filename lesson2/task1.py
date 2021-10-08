"""
1 Даны кортеж пользователей users и набор шаблонов templates
Задача обращаясь по индексу к кортежу пользователей напечатать на экране сообщение
если пользователю менее 7 лет: "{name} {surname} закончил школу"
Внимание конструкцию IF ELSE мы не используем (мы ее еще не изучали, и даже если знаете не используйте)
"""

users = (
    {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)

user_1 = (users[0]["age"] < 7)
result_1 = templates[user_1].format(
    name=users[0]["name"],
    surname=users[0]["surname"]
)

user_2 = (users[1]["age"] < 7)
result_2 = templates[user_2].format(
    name=users[1]["name"],
    surname=users[1]["surname"]
)

print(f'{result_1}\n{result_2}')
