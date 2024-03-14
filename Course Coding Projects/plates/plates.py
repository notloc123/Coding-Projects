import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Inserts plate paramter into function as variable (s)
def is_valid(s):
    # Checks if length of plate is under two or over 6 characters and checks if first two characters are numbers, if they are it returns a False value
    if s[1:2].isdigit() == True or len(s) < 2 or len(s) > 6:
        return False
    # Checks for blank spaces in any part of the plate and returns a False value if true
    for blank in s:
        if blank in [" "]:
            return False
    # Defines parameter "found_number" as a boolean(T/F) statement that is False
    # For/in statement that is "walking the string" to analyze each character in the string starting from the 2 position.
    found_number = False
    for char in s[2:]:
        # Checks char in string to see if it is punctuation, is so, it returns False
        if char in string.punctuation:
            return False
        # Checks char to see if it is a digit, and changes "found_number" to True if not a "0" to invalidate starting with a "0"
        elif char.isdigit() and char != '0':
            found_number = True
        #Checks that char is a "0" AND NOT True, if not both, returns False
        elif char == '0' and not(found_number):
            return False
        # Checks char if it's an alpha AND the state of "found_number", if an alpha and also True, returns False
        elif char.isalpha() and found_number:
            return False
    else:
        return True

main()