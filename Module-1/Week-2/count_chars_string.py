def exercise2(str):
    dict = {}
    for char in str:
        dict[char] = str.count(char)
    return dict

print(exercise2("Happiness"))
print(exercise2("smiles"))
