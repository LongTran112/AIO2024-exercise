def excercise1(num_list, k):
    result = None
    for i in range(len(num_list) - k + 1):
        sliding_window = num_list[i: k + i]
        result = max(sliding_window)
        print(result)
    return result

print(excercise1([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1], 3))
