#### IP Checker

Showcases usage of regular expressions to check if an IPv4 address is valid.

### def validate
Uses re.search(regex) to check the IP address using parametes in a regular expression.
If the string does not match the expression, it will return False.
The string will be split using "." as the divider and each octet will be check for the proper value (between 0 and 255) and will return False if an invalid number is detected.

#### Test IP Checker

Tests the numb3rs.py file and will import the validate  function from numb3rs.py.
The format of the IPv4 address will be asserted and the validate function will check each type.
The range will be asserted and each octetwill be checked to be a proper number.