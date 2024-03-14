import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        number_list = ip.split(".")
        for number in number_list:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
