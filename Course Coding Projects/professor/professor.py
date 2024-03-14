# Imports the randrange function from the random library
from random import randrange

# Defines the function main()
#   level is the function get_level()
#   score is the function games(level) with level inserted as arguement
#   after games() runs it will print the player score using the returned 'score' variable and exit the program
def main():
    level = get_level()
    score = games(level)
    print("Score:", score)
    exit()

# Defines get_level() function
#   While True loop started
#       try
#           level which is the integer of the user input
#           if user input (level) is 1, 2, 3 it will break loop else it will pass which will reprompt
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level

# Defines generate_integer(level) with level argument passed into it
#   if level is 1 it will assign variables x, y with single digit numbers
#   if level is 2 it will assign x, y with double digit numbers
#   if level is 3 it will assign x, y with triple digit numbers
#   x, y values  are returned
def generate_integer(level):
    if level == 1:
        x = randrange(0, 10)
        y = randrange(0, 10)
    elif level == 2:
        x = randrange(10, 100)
        y = randrange(10, 100)
    elif level == 3:
        x = randrange(100, 1000)
        y = randrange(100, 1000)
    return x, y

# Defines round(x, y) function with arguements x, y passed into it
#   count is defined as a value of 1
#   while count is <= 3 it will try
#       define attempt as an integer of a user input with variables x, y placed to form the equation
#       if user attempt == (x + y) then it returns True to exit function
#       else the count is increased by 1 and "EEE" is printed
#       the exception is if count > 3 it will print the full equation AND the answer and return False
def round(x, y):
    count = 1
    while count <= 3:
        try:
            attempt = int(input(f"{x} + {y} = "))
            if attempt == (x + y):
                return True
            else:
                count += 1
                print("EEE")
        except:
            count += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

# Defines games(level) function with level arguement passed into it
#   game_count defined as having a value of 1
#   score is given a value of 0
#   while game_count <= 10 it will enter loop
#       x, y variables are given a random integer using the generate_integer(level) function with level passed into it so the correct numbers are returned based on the level
#       answer is defined as the round(x, y) function with variables x, y passed into it to determine what that specific round's equation and answer will be
#       if answer is returned as True, score is increased by 1
#       game_count increases by 1 regardless of True/False return value
#   when game_count > 10 it will return the score variable
def games(level):
    game_count = 1
    score = 0
    while game_count <= 10:
        x, y = generate_integer(level)
        answer = round(x, y)
        if answer == True:
            score += 1
        game_count += 1
    return score

if __name__ == "__main__":
    main()