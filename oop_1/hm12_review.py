from collections import defaultdict

dictionary = defaultdict(set)

dictionary["user"].add((1, 2))
dictionary["user"].add((2, 2))
print(dictionary)
