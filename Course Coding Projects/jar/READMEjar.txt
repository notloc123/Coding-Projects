#### Cookie jar

This is a project to showcase creating a class with properties that can be modified and can retain data within the file and can be accessed through user input.

### Jar Class
Class "Jar" is created and in this case is manually set to a capacity of "12" and if the capacity is set to less than "0" then it will raise a ValueError and print "NO COOKIES."
The size of the of Jar starts at "0" and is modified through the user input.
## def deposit
def deposit(self, n) checks if n or self.size + n is larger than capacity and will raise a ValueError and print "TOO MANY COOKIES" if the deposit amount exceeds capacity.
If capacity is not exceeded, 
## def withdraw
def withdraw(self, n) checks if n is greater than self.size and will raise ValueError and print "NOT ENOUGH COOKIES LEFT" if withdrawal amount exceeds current cookies count.

### def main()
Will use print function to display options for the user to enter and act as a menu to reach other functions.
The menu items displayed correspond to the above functions and require user input, except "c - check cookies" which will display the amount of cookies currently deposited.
To exit function would be to type "exit" from the programs "main menu"

#### Test Jar

This imports the Jar class from jar.py and for the purpose of this will test initilizing the Jar class with a capacity of "12" which was set manually earlier.

### test_str
Creates an "empty" Jar and tests the display of cookies starting with "0" cookies and adding more until at the "12" capacity.

### test_deposit
Creates an "empty" Jar and tests the deposit function to adjust jar.size to correct amount.

### test_withdraw
Creates an "empty" Jar and deposits "2" and tests if withdraw function will remove correct amount.