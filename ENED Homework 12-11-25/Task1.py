import random as r
import math as m
def estimate():
    p = 0
    while True:
        n = int(input("enter a number pls\n"))
        if n > 0:
            break
        else:
            print("please enter a valid integer\n-1")
    for i in range(n):
        y = r.random()
        x = r.random()
        if (x**2 + y**2) <= 1:
            p += 1
    hmm = (p / n) * 4
    diff = abs(hmm - m.pi)
    print(f"with {n} number of points, the difference between the estimated pi and the 'real' value is {diff:.7f}")
estimate()