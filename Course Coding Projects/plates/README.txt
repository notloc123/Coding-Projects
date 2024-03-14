#### Vanity Plate Checker

This project is designed to check plates from the initial submission of the plate.
Plates will need to follow Massachusetts guidelines such as:
- Must start with at least two letters
- Minimum 2 characters and maximum 6 characters long
- No numbers preceeding a letter
- First number cannot be "0"
- No periods, spaces, or punctuation

### main 

Requests the plate input from the user and will check with the is_valid function.
If valid, it will print "Valid" and if invalid will print "Invalid."

## is_valid
First checks that the first two characters are not digits and that the length falls between 2 and 6 characters long.
Second check will look for any black spaces in the user input
Third check sets a new variable as found_number = False and as the functions "walks the string," if it sees a number, it will change to True and if a letter is found while True, will return an Invalid plate. 
As the string is walked, it will look for a leading "0" and will check for any punctuation. If all passes, it will return True for a valid plate.

#### Test Plates

Imports the is_valid function from plates.py and will test individual portions of the is_valid function. Each function will test different inputs from the user as "assertions."