def print_matrix(matrix):
    print("\n".join([" ".join(map(str, row)) for row in matrix]))

def excercise4(str1, str2):
    # plus 1 for empty string matrix
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # create 2D matrix with list comprehension
    # create column by row
    matrix = [[0 for _ in range(len_str2)] for _ in range(len_str1)]

    print_matrix(matrix)
    print("===========")

    # Initialize matrix
    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j

    print_matrix(matrix)
    print("===========")

    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i-1][j] + 1,
                               matrix[i][j-1] + 1,
                               matrix[i-1][j-1] + cost)


    return matrix[-1][-1]

str1 = "kitten"
str2 = "sitting"
distance = excercise4(str1, str2)
print(f"Levenshtein distance between '{str1}' and '{str2}' is {distance}")

