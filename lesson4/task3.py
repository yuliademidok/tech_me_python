"""
Имеется 2 кортежа с координатами Ферзя и Пешки на шахматной доске
Определить Бьет ли Ферзь пешку
координаты хранятся (x, y)
"""

queen = (4, 2)
pawn = (7, 5)

result = queen[0] == pawn[0] or \
         queen[1] == pawn[1] or \
         (abs(queen[0] - pawn[0]) == abs(queen[1] - pawn[1]))

print(result)
