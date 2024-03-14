# defines the dictionary "shop_list" outside of the loop so it can be updated inside the loop
shop_list = {}

# Puts user in loop that will wait for input.
while True:
    try:
        # Defines user input as item and capitalizes it
        item = input().upper()
        # If user input "item" is in {shop_list} it will add 1 to the values
        if item in shop_list:
            shop_list[item] = shop_list[item] + 1
        # If the user input "item" is not in {shop_list} it will create a key with a value of [1] and remprompt user
        else:
            shop_list[item] = 1
    # When user presses "CTRL+D" it willbreak the loop and print the value of each item entered. in the format [Value], Key
    except EOFError:
        for i in sorted(shop_list):
            print(shop_list[i], i)
        break

