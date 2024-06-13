def excercise5(y, y_hat, n, p):
    return pow(pow(y, 1/n) - pow(y_hat, 1/n),p)

print(excercise5(100, 99.5, 2, 1))