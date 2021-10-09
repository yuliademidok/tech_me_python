"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
"""
seasons = ['',
           'зима', 'зима',
           'весна', 'весна', 'весна',
           'лето', 'лето', 'лето',
           'осень', 'осень', 'осень',
           'зима']


month = input("Enter month number\n>>>")

if month.isdigit() and int(month) in range(1, 13):
    result = seasons[int(month)]
else:
    result = "No such month found"

print(result)
