import random 
import math

def MAE(sample_size):
    result = 0

    for i in range(sample_size+1):
        target = random.uniform(0,10)
        prediction = random.uniform(0,10)
        loss = abs(target - prediction)
        print("loss name: {}, sample: {}, pred: {}, target: {}, loss: {}".format("MAE", i, prediction, target, loss))
        result = result + loss

    return result/sample_size

def MSE(sample_size):
    result = 0

    for i in range(sample_size+1):
        target = random.uniform(0,10)
        prediction = random.uniform(0,10)
        loss = pow(target - prediction, 2)
        print("loss name: {}, sample: {}, pred: {}, target: {}, loss: {}".format("MSE", i, prediction, target, loss))
        result = result + loss

    return result/sample_size

def RMSE(sample_size):
    return math.sqrt(MSE(sample_size))


def excercise3():
    sample_size = input("Input number of samples (integer number) which are generated:")
    if(not sample_size.isnumeric):
        print("number of samples must be an integer number")
        return
    
    loss_name = input("Input loss name:")

    sample_size = int(sample_size)

    if(loss_name == "MAE"):
        return MAE(sample_size)
    elif(loss_name == "MSE"):
        return MSE(sample_size)
    elif(loss_name == "RMSE"):
        return RMSE(sample_size)
    else:   
        return "Loss name not supported"
    
print("final loss: {}".format(excercise3()))