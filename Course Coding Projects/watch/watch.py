# Imports the re library
import re

# defines the main() function
# prints the output of parse(input) functions
def main():
    print(parse(input("HTML: ")))

# Defines the parse(s) function
# If re.search is (regex, s) then will move to next if statement
# if url := (regex, s, re.IGNORECASE) then move to next line
#   regex statement does not store some values so that url_group[1] will be the last part of the link
# will return a string concatinated with url_group[1]
def parse(s):
    if re.search(r"<iframe(.)*></iframe>", s):
        if url := re.search(r"(?:http(s?)*://(?:www\.)*youtube\.com/embed/)([a-z0-9]+)", s, re.IGNORECASE):
            url_group = url.groups()
            return "https://youtu.be/" + url_group[1]


if __name__ == "__main__":
    main()
