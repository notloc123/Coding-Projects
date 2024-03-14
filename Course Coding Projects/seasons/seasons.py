from datetime import date
import inflect
import sys
i = inflect.engine()

def main():
    today, dob = get_date()
    minutes = do_math(today, dob)
    result = i.number_to_words(minutes, andword="")
    print(result.capitalize(), "minutes")

def get_date():
    iso_dob = input("Date of Birth: ")
    iso_today = str(date.today())
    check_format(iso_dob)
    check_format(iso_today)
    if check_format(iso_dob) == False:
        sys.exit("Invalid date")
    year1, month1, day1 = split_date(iso_today)
    year, month, day = split_date(iso_dob)
    dob = date(year, month, day)
    today = date(year1, month1, day1)
    return today, dob

def check_format(s):
    try:
        if "-" not in s:
            raise ValueError
        date.fromisoformat(s)
        return True
    except ValueError:
        return s == False
        # sys.exit("Invalid date")

def split_date(x):
    year, month, day = x.split("-")
    return int(year), int(month), int(day)

def do_math(today, dob):
    difference = today - dob
    minutes = difference.days * 24 * 60
    return minutes

if __name__ == "__main__":
    main()
