""""
Коллекции:
list - not hashable
tuple - hashable, not hashable is there is list inside
str - immutable data type

dict - key can be only hashable value, not hashable
set - not subscrible, not hashable, cannot contain not hashable values
frozenset
"""

"""
x = (1, 2, 3, 4, 5, 6)
a, b, *c = x
c
[3, 4, 5, 6]
------------
a, b, *c = x
c
[3, 4, 5, 6]
x = (1, 2, 3, 4, 5, 6)
a, b, *_ = x - мусор
------------
d = {True: "Hello", 1: "bye"}
d
{True: 'bye'}
------------
bio = "{0} {1} {2} some text"
bio.format(a, b , c)
------------
bio = "{name} {surname} {date} some text"
bio.format(name=a, surname=b, date=c)
"""
