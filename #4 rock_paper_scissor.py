import random

# a function that generates random values of "rock","paper",and "scissor"

def random_generator():
    option = ["rock","paper","scissor"]
    result = random.choice(option)
    return result

x = random_generator()
guess = input("Enter your guess : ").lower()

# a function to take a guess from the user and compare with the random value generated

def user(guess : str):
    if guess == "rock" and x == "paper":
        return "you loose"
    elif guess == "rock" and x == "scissor":
        return "you won"
    elif guess == "paper" and x == "scissor":
        return "you loose"
    elif guess == "paper" and x == "rock":
        return "yow won"
    elif guess == "scissor" and x == "paper":
        return "you won"
    elif guess == "scissor" and x == "rock":
        return "you loose"
    elif guess == x:
        return "draw"
    
#calling the functions
print(user(guess))





