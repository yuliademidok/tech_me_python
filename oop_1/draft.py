# import re
#
# text = "Hello.World"
# text = "Hello world"
# text = " a word "
# text = "... and so on ..."
#
# result = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\\\:"|<,./<>? ]', text)
# result = list(filter(None, result))
# print(result)


from datetime import datetime

from datetime import date, timedelta

# f = date(2014, 12, 31) # 31 december 2014
# s = date(2011, 1, 1) # 1 january 2011
# f - s == datetime.timedelta(1460)


# def days_diff(a, b):
#     a = date(*a)
#     b = date(*b)
#     # a = datetime.strptime(", ".join(map(str, a)), "%Y, %m, %d")
#     # b = datetime.strptime(", ".join(map(str, b)), "%Y, %m, %d")
#     c = b - a
#     return c.days
#
#
# print(days_diff([1982,4,19], [1982,4,22]))



