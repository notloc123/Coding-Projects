import sys

class Jar:
	def __init__(self, capacity=12):
		if capacity < 0:
			raise ValueError("NO COOKIES")
		self._capacity = capacity
		self._size = 0

	def __str__(self):
		return self.size * "🍪"

	def deposit(self, n):
		if n > self.capacity or self.size + n > self.capacity:
			raise ValueError("TOO MANY COOKIES")
		self._size += n

	def withdraw(self, n):
		if self.size < n:
			raise ValueError("NOT ENOUGH COOKIES LEFT")
		self._size -= n

	@property
	def capacity(self):
		return self._capacity

	@property
	def size(self):
	    return self._size
jar = Jar()

def main():
    print("Welcome to the cookie bank. What would you like to do?")
    print("c - check cookies")
    print("d - deposit cookies")
    print("w - withdraw cookies")
    print("exit - leave bank")
    print()
    action = input().lower().strip()
    if action not in ["c", "d", "w", "exit"]:
        main()
    if action == "c":
        get_cookie_count()
    if action == "d":
        deposit_cookie()
    if action == "w":
        withdraw_cookie()
    if action == "exit":
        sys.exit("Thank you for visting the cookie bank")


def get_cookie_count():
    print()
    print(jar)
    print()
    main()

def deposit_cookie():
    print()
    amount = int(input("How many? "))
    jar.deposit(amount)
    main()

def withdraw_cookie():
    print()
    amount = int(input("How many? "))
    jar.withdraw(amount)
    main()


if __name__ == "__main__":
	main()
