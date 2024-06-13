def f1_score(tp, fp, fn):
    def precision(tp, fp):
        precision = tp/(tp+fp)
        print("Precision value: {}".format(precision)) 
        return precision

    def recall(tp, fn):
        recall = tp/(tp+fn)
        print("Recall value: {}".format(recall))
        return recall

    precision = precision(tp, fp)
    recall = recall(tp, fn)
    f1_score = 2*(precision * recall)/(precision + recall)
    
    print("F1 Score value: {}".format(f1_score)) 
    return f1_score

def check_type(input):
    if(type(input) != int):
        return False
    return True

def excercise1(tp, fp, fn):
    
    if(check_type(tp) == False):
        print("tp must be of type int")
        return
    if(check_type(fp) == False):
        print("fp must be of type int")
        return
    if(check_type(fn) == False):
        print("fn must be of type int")
        return

    if(tp <= 0 or fp <=0 or fn <=0):
        print("tp and fp and fn must be greater than zero")
        return

    
    return f1_score(tp, fp, fn)

excercise1(2, 4, 5)
excercise1("A", 3, 4)

print("==========")
assert round(excercise1(2, 3, 5), 2) == 0.33, "The result is not 0.33"
print("==========")
print(round(excercise1(2, 4, 5), 2))