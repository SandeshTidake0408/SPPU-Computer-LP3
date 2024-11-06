import numpy as np


def function(x):
    return (x+3) ** 2


def gradient(x):
    return 2 * (x+3)


def gradient_descent(start, learning_rate, iterations):
    x = start
    for i in range(iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        print(f"Iteration{i+1} : x = {x}, f(x) = {function(x)}")
    return x

start = 2.0
learning_rate = 0.1
iterations = 20

print(gradient_descent(start, learning_rate, iterations))