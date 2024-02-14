
#  !!!!!!!!!!!!!!!!!!!! INCOMPLETE !!!!!!!!!!!!!!!1

""" project #1 from the book "The Big Book Of Small Python Projects" """
import random
res = 0
"""generating a random number """
a = random.randint(0,11)
b = random.randint(0,11)
c = random.randint(0,11)
"""assigning a,b and c into an empty list called answer"""
answer = [a, b, c]
x = 1
while x in range(0,11):
    c = int(input("First number : "))
    d = int(input("Second number : "))
    e = int(input("Third number : "))
    guess = [c, d, e]
    for i in range(3):
        for j in range(3):
            if guess[i] == answer[j] and i == j:
                res = "pico"
                break
            elif guess[i] == answer[j] and i != j:
                res = "fermi"
                break
            else :
                res = "wrong"

        print(res)
    print(f"the guess: {guess}")
    print(answer)
    if a == c and b == d and c == e :
        break
