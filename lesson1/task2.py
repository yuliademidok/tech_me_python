from datetime import date


name = "Василий"
surname = "Иванов"
age = 33
height = 182

current_year = date.today().year
birth_year = current_year - age
bio = name + " " + surname + " " + str(birth_year) + " " + "ростом" + " " + str(height) + " " + "см"
print(bio)
