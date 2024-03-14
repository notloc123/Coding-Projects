# Lines 1-3 import the json, requests, sys libraries.
import json
import requests
import sys

# Defines the function digit_check(user_input)
# user_input is defined as user_input.isalpha() to check if input
# if the user_input.isalpha() returned True
#   prints the given prompt then exits program
# if user_input.isalpha() returned False
#   returns False and exits loop
def digit_check(user_input):
    user_input = user_input.isalpha()
    if user_input == True:
        print("Command-line arguement is not a number")
        sys.exit(1)
    if user_input == False:
        return False

# Defines the function get_total(user_input)
# response is defined as the request.get("source")
# jason is defined as the response.json()
# pretty_jason is defined as the specified "jason"
# total = pretty_jason * user_input
# prints the total amount converted into a dollar amount
def get_total(user_input):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    jason = response.json()
    pretty_jason = jason["bpi"]["USD"]["rate_float"]
    total = pretty_jason * user_input
    print(f"${total:,.4f}")

# Defines the main() function
# defines user_input as sys.argv[1]
# calls function digit_check(user_input) with user_input as the arguement
# defines user_input as a float
# calls function get_total(user_input) with user_input as the arguement
def main():
    user_input = sys.argv[1]
    digit_check(user_input)
    user_input = float(user_input)
    get_total(user_input)

if __name__ == "__main__":
    main()