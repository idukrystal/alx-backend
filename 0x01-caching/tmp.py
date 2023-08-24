
dict = {
    "a": 2,
    "c": 3,
    "b": 1,
    "d": 4
}

print(sorted(dict.items(), key = lambda item : item[1], reverse = True)[0][0])
