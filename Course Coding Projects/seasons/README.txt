#### Time Difference

Prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals.

### functions

## main

Calls the functions and then will convert the result of do_math into words using inflect. The result will be printed.

## get_date 

Gets the date of birth of a user in the form of a user prompt and will fetch today's date as a string, calls the check_format function.
"Today" and user's "dob" will be split into three variables: year, month, day using split_date.

# check_format 

checks to make sure the date is formatted in YYYY-MM-DD.

# split_date

splits the date by the "-"

## do_math

Called by main to get the difference between today and the dob and will conver that into minutes.