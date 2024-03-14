import sys

def main():
    check_length(sys.argv[1:])
    check_file(sys.argv[1])
    try:
        file_name = open(sys.argv[1])
        lines = file_name.readlines()
        check_line(file_name)
        line_count = 0
        for line in lines:
            if check_line(line) == False:
                line_count += 1
        print(line_count)
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_file(x):
    if x.endswith(".py"):
        return True
    else:
        sys.exit("Not a Python file")

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

def check_line(line):
    line = ''.join(line)
    if line.isspace() or line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
