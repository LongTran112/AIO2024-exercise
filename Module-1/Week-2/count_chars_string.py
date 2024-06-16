def exercise2(str):
    dict = {}
    for char in str:
        dict[char] = dict.get(char, 0) + 1
    return dict

print(exercise2("Happiness"))
print(exercise2("smiles"))
print(exercise2("Baby"))
print(exercise2("smiles"))