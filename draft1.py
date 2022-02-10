def checkio(data):
    data = sorted(data)
    alphabet = [i for i in data.pop(0)]
    start = 0

    while data:
        data_elem = data.pop(0)

        for i in data_elem:
            if i in alphabet:
                start = alphabet.index(i)
                edge = data_elem[:data_elem.index(i)]

                if start == 0 or data_elem[0] == " ":
                    alphabet.insert(start, edge)
                else:
                    data.append(" " + data_elem)

                data_elem = data_elem.replace(edge, " " * len(edge))

        if data_elem[-1] == " " or start + 1 == len(alphabet):
            alphabet.insert(start + 2, data_elem)
        else:
            data_elem += " "
            data.append(data_elem.lstrip(" "))

        arr_split = []
        for i in alphabet:
            arr_split.extend(list(i))
        alphabet = list(filter(lambda x: x != " ", arr_split))

    return "".join(list(dict.fromkeys(alphabet)))


print(checkio(["is", "not", "abc", "nots", "iabcn"])) # iabcnots ['abc', 'iabcn', 'is', 'not', 'nots']
# print(checkio(["klm", "kadl", "lsm"])) # kadlsm  ['kadl', 'klm', 'lsm']
# print(checkio(["xxxyyz", "yyww", "wwtt", "ttzz"])) # xywtz  ['tz', 'wt', 'xyz', 'yw'] wtz
# print(checkio(["ghi", "abc", "def"])) # abcdefghi
# print(checkio(["b", "d", "a"])) # abd
# print(checkio(["my", "name", "myke"])) # namyke
# print(checkio(["dfg", "frt", "tyg"])) # dfrtyg
# print(checkio(["acb", "bd", "zwa"])) # zwacbd
