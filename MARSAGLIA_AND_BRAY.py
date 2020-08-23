import random
import math
import numpy as np

# x = random.uniform(0, 1)

prob = random.random()

u1 = random.uniform(0, 1)
u2 = random.uniform(0, 1)
u3 = random.uniform(0, 1)

print("Random float number is ", prob)
print("Random float number is ", u1)
print("Random float number is ", u2)
print("Random float number is ", u3)

def g(temp):
    if (abs(temp) < 1):
        return 17.49731196 * math.exp(-0.5*pow(temp, 2)) - 4.73570326(3 - pow(temp, 2)) - 2.15787544(1.5 - abs(temp))
    if (abs(temp) < 1 & abs(temp) < 1.5):
        return 17.49731196 * math.exp(-0.5 * pow(temp, 2)) - 4.73570326(3 - pow(temp, 2)) - 2.15787544(1.5 - abs(temp))
    if (abs(temp) < 1.5 & abs(temp) < 3):
        return 17.49731196 * math.exp(-0.5 * pow(temp, 2)) - 4.73570326(3 - pow(temp, 2))
    if (abs(temp) < 3):
        return 0

if (prob < 0.8638):
    X = 2.0*(u1 + u2 + u3 - 1.5)
elif(prob < 0.9745):
    X = 1.5*(u1 + u2 - 1)
elif(prob < 0.9973002039):
    while True:
        x = 6*u1 - 3
        y = 0.358*u2
        if (y < g(x)):
            break
        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)
elif(prob < 1):
    while True:
        v1 = random.uniform(-1, 1)
        v2 = random.uniform(-1, 1)

        x = v1 * ((9 - math.ln(v1**v1 + v2**v2))/(v1**v1 + v2**v2))**0.5
        y = v2 * ((9 - math.ln(v1**v1 + v2**v2))/(v1**v1 + v2**v2))**0.5

        if (x > 3 | y > 3):
            if(x > 3):
                X = x
            else:
                X = y
            break


print(X)
