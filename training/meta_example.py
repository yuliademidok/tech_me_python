# class Meta(type):
#     def create_local_attrs(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value
#
#     def __init__(cls, name, bases, attrs):
#         cls.class_attrs = attrs
#         cls.__init__ = Meta.create_local_attrs
#
#
# class People(metaclass=Meta):
#     name = "Bob"
#     age = 12
#     sex = "M"
#
#
# w = People()
# print(w.class_attrs)


###
# def create_class_point(name, base, attrs):
#     attrs.update({"MAX_COORD": 3, "MIN_COORD": 2})
#     return type(name, base, attrs)

class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({"MAX_COORD": 3, "MIN_COORD": 2})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 3
    #     cls.MIN_COORD = 2


class Point(metaclass=Meta):

    def get_coords(self):
        return self.MAX_COORD + self.MIN_COORD


p = Point()
print(p.MAX_COORD)
print(p.get_coords())
