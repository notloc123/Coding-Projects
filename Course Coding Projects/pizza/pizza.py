# Imports the sys, csv libraries and tabulate from the tabulate library
import sys
import csv
from tabulate import tabulate

# Defines the function main()
# calls check_length(sys.argv[1:]) which checks the length of the command line arguement
# calls check_file which will check for the proper file type
# file_name is defined as the 1st command line arguement after the checks are done
# calls turn_table(file_name) that will turn the file_name into a ASCII table with the information
def main():
    check_length(sys.argv[1:])
    check_file(sys.argv[1])
    file_name = sys.argv[1]
    turn_table(file_name)

# While True loop to check for too few/many arguements and exit with prompt
# If arguement == 1 then break loop and continue code
def check_length(check_input):
    while True:
        if len(check_input) < 1:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(check_input) > 1:
            print("too many command-line arguements")
            sys.exit(1)
        elif len(check_input) == 1:
            break

# checks the file type
# try if file endswith .csv it will return True and continue with code
# else it will return False and exit code with prompt
# In case of FileNotFoundError, it will exit with prompt
def check_file(x):
    try:
        if x.endswith(".csv"):
            return True
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

# Defines pizza as an empty list to be appended later
# opens "y" (file_name) as variable csvfile
# uses csv.reader(csvfile) to read and append rows to pizza = []
# will print the appended rows using the tabluate function and defining the "pizza" table
def turn_table(y):
    pizza = []
    with open(y) as csvfile:
        for row in csv.reader(csvfile):
            pizza.append(row)
    print((tabulate(pizza[1:], headers=pizza[0], tablefmt="grid")))


if __name__ == "__main__":
    main()
