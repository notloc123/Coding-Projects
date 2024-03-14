# Imports randrange function from the random library
from random import randrange

# Defines the function main()
#   Starts try/except
#       Starts While True loop
#           defines parameter "level" as a user input as an integer
#           defines "guess" as a randrange of "level" + 1
#           if level is <= 0 then it will reprompt the user input by calling the main() function again
#           else it will break out of the While True loop and continue down the funciton
#       Starts While True loop
#           defines "player_guess" as user input as in integer
#           if "player_guess" is > "level" it will raise a ValueError and reprompt user by calling main() function
#           elif "player_guess" is < "guess" it will print "Too small!" and reprompt user for another "player_guess"
#           elif "player_guess" is > "guess" it will print "Too large!" and reprompt user for another "player_guess"
#           elif "player_guess" is == "guess it will print "Just right!" and quit the program
def main():
    try:
        while True:
            level = int(input("Level: "))
            guess = randrange(1, level + 1)
            if level <= 0:
                raise main()
            else:
                break

        while True:
            player_guess = int(input("Guess: "))
            if player_guess > level:
                return True
            elif player_guess < guess:
                print("Too small!")
            elif player_guess > guess:
                print("Too large!")
            elif player_guess == guess:
                print("Just right!")
                quit()
    except ValueError:
        raise main()

main()