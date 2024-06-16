def excercise1(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        sliding_window = num_list[i: k + i]
        result.append(max(sliding_window))
    return result

print(excercise1([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1], 3))
print("====")
print(excercise1([3 , 4 , 5 , 1 , -44],3))
print("====")
print(excercise1([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1],3))