def factorial(num):
    if(num == 1):
        return 1
    if(num == 0):
        return 1
    return num*factorial(num-1)

def approx_sin(radian, n):
    result = 0
    for i in range(n+1):
        result = result + (((-1)**i)*pow(radian, 2*i + 1)/factorial(2*i +1))
    return result

def approx_cos(radian, n):
    result = 0
    for i in range(n+1):
        result = result + (((-1)**i)*pow(radian, 2*i)/factorial(2*i))
    return result

def approx_sinh(radian, n):
    result = 0
    for i in range(n+1):
        result = result + (pow(radian, 2*i+1)/factorial(2*i +1))
    return result

def approx_cosh(radian, n):
    result = 0
    for i in range(n+1):
        result = result + (pow(radian, 2*i)/factorial(2*i))
    return result

print(approx_sin(3.14, 10))
print(approx_cos(3.14, 10))
print(approx_sinh(3.14, 10))
print(approx_cosh(3.14, 10))

print("=========")

print(round(approx_cos(3.14, 10),2))
print(round(approx_sin(3.14, 10),4))
print(round(approx_sinh(3.14, 10),2))
print(round(approx_cosh(3.14, 10),2))