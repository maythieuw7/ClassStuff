# This script uses a for loop in order to calculate the factorial of a number
def fact():
    num, n = 1, int(input("What number do you want to calculate the factorial of?\n"))
    if n == 0:
        return print(1)
    elif n < 0:
        return print("enter a positive number")
    for i in range(n):
        i += 1
        num *= i
    return print(num)

# This script simulates a coinflip
import random as r
def flip():
    h, t, n, tt = 0, 0, int(input("How many times do you want to flip the coin?\n")), 0
    for i in range(n):
        tt += 1
        num = r.randint(1,2)
        if num == 1:
            h += 1
        else:
            t += 1
    return print(f"{((h/tt) * 100):.1f}% heads, {((t/tt) * 100):.1f}% tails")

# This script does whatever madness the jacobsthal sequence is (this took a lot to figure out ngl)
def IDoNotLikeThis():
    seq, prepre, pre, = [0], 0, 1
    while True:
        n = int(input("Enter an integer\n"))
        if n <= 0:
            print("Uhhh you were lowkey not supposed to enter this kinda number try again")
        elif n == 1:
            return print(seq)
        else:
            break
    seq.append(1)
    #okay now we try to do this like J(n) = J(n-1) + 2 * J(n-2) or whatever this is
    for i in range(n-2):
        cur = pre + 2 * prepre
        seq.append(cur)
        prepre = pre
        pre = cur
    return print(f"Here are the terms bru {seq}")

# Okay so this was a lot easier than the last one (i am saying before writing this) we are going to estimate pi with the leibniz formula which I found online
import math as m
def ESTIMATE():
    pie = 1
    #okay so we gonna use 4 * (1 - 1/3 + 1/5 - 1/7...) type thing
    # this is like -1**n * (1 / (3 + 2(n-1))) i think
    while True:
        n = int(input("how many terms do you want to use to estimate pi? (1 not included)\n"))
        if n == 0 or n <= 0:
            print("Why would you even type that ur the reason I gotta write this failsafe man pls try again\n")
        else:
            print("thank you for using an actual number")
            break
    #now we calculate
    for i in range(n):
        i += 1
        pie += (((-1)**i) * (1 / (3 + (2 * (i-1)))))#i wonder if I used enough parenthesis
    return print(f"The difference between the estimation of pi and the value from the math library for {n} terms is {(4*pie)-m.pi}\nAlso the percent error is {(abs((4*pie - m.pi)/m.pi) * 100)}%")
