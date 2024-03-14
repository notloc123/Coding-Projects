# Imports the sys and csv libraries
import sys
import csv

# Defines the main() function
# calls check_length(sys.argv[1:]) that checks for the appropriate amount of arguments
# calls check_file(sys.argv[1], sys.argv[2]) to check if they are .csv files
# defines file_1, file_2 as both sys.argv [1] and [2]
# calls modify_file(file_1, file_2) that will take before.csv and create a new "after.csv" with in order of First, Last, House
def main():
    check_length(sys.argv[1:])
    check_file(sys.argv[1], sys.argv[2])
    file_1, file_2 = sys.argv[1], sys.argv[2]
    modify_file(file_1, file_2)

# Defines modify_file(file_1, file_2) function
# defines name_list as an empty list
# try:
# opens file_1 as csvfile
# defines reader variable as csv.DictReader which creates a dictionary object for each row
# for each row in reade
# name_order will be defined as the row["name"] and splits it by ","
# appends to name_list the name_order[1] as "first", name_order[0] as "last", and house as "house"
    # This is just reordering the first and last names of the list while keeping "house" as last
# if FileNotFound, will exit program with prompt
# opens(file_2) with "w" write function as new_file
    # In this case,there is no file to write to so one will be created
# new_dict is defined as csv.DictWriter(csvfile) which will write the dictionary object for each row
# for row in reader
# name_order is row["name"] split by ","
# name_list is appended using the named keys
def modify_file(file_1, file_2):
    name_list = []
    try:
        with open(file_1) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name_order = row["name"].split(",")
                name_list.append({"first": name_order[1].lstrip(),"last": name_order[0].lstrip(), "house": row["house"]})
    except FileNotFoundError:
        sys.exit("Could not read",file_1)
    with open(file_2, "w") as new_file:
        new_dict = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
        new_dict.writerow({"first": "first", "last": "last", "house": "house"})
        for row in name_list:
            new_dict.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

# Defines the check_length(check_input) function
# While true loop
# if the len of check_input is > or < 2, will exit with prompt
# elif the len == 2 then will break loop
def check_length(check_input):
    while True:
        if len(check_input) < 2:
            sys.exit("Too few command-line arguments")
        elif len(check_input) > 2:
            sys.exit("Too many command-line arguements")
        elif len(check_input) == 2:
            break

# Defines check_file(x, y) function
# try:
# if ".csv" is not in x or y, will exit with prompt
# exception of a FileNotFoundError
def check_file(x, y):
    try:
        if ".csv" not in x or ".csv" not in y:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
