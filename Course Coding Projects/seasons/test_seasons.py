from seasons import check_format

def main():
    check_format()

def test_check_format():
    assert check_format("1997-01-23") == True
    assert check_format("01231997") == False
    assert check_format("January 23, 1997") == False

if __name__ == "__main__":
    main()
