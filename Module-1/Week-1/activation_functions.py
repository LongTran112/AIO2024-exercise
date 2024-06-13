import math

# Given
def is_number(n): 
    try:
        float(n)
        # Type-casting the string to ‘float‘. # If string is not a valid ‘float‘,
        # it’ll raise ‘ValueError ‘ exception
    except ValueError: 
        return False
    return True

def check_activation_function(string, number):
    if(string == "sigmoid"):
        return sigmoid(number)
    elif(string == "relu"):
        return relu(number)
    elif(string == "elu"):
        return elu(number)
    else:
        print("{string} is not supported")
        return

def sigmoid(number):
    return (1/(1+pow(math.e, -number))) 

def relu(number):
    if(number <= 0):
        return 0
    return number

def elu(number):
    alpha = 0.01
    if(number <= 0):
        return alpha*((math.e ** number)-1)
    return number


def excercise2():
    input_number = input("Please enter your x value:")
    if(not is_number(input_number)):
        print("x must be a number")
        return 

    number = float(input_number)

    activation_function = input("Please enter your activation function (sigmoid, relu, elu):")

    return check_activation_function(activation_function, number)


result = excercise2()
if(result != None):
    print(round(result,2))

