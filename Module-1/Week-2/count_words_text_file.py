
def excercise3():
    dict = {}
    with open("P1_data.txt", "r") as file:
        content = file.read()
        # Pre-processing data
        content = content.replace(",", " ")
        content = content.replace(".", " ")
        content = content.replace("-", " ")
        content = content.lower()
        content = content.split()
        # Convert data to list
        content = list(content)
        # Word Occurrence Count in data 
        for word in content:
            dict[word] = dict.get(word, 0) + 1

    return dict

dict = excercise3()

for key, value in dict.items():
    print(f"{key}: {value}")

print(dict["man"])

