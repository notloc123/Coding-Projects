#### Line Reader

This project was designed to count the lines of code in a another .py file. This program will not count blank lines and will exclude lines that are commented out by using the "#" symbol.

## main

Call the check_length, check_file, and check_line functions. It will open the requested file and begin counting the lines. If all checkes are passed this will return a line count of the requested .py file. 

## check_length

Checks the length of the command-line arguement. This is specifically designed to take in a single arguement starting at sys.argv[1].

## check_file

This function soley checks the extension to determine if the file ends with ".py"

## check_line

This function checks if a line is blank or starts with "#" and will return True if so, and will not add to the line count.