    # The Discourse Bot
    #### Video Demo:  https://youtu.be/vrkyNKbnJx8
    ### Description:
    I have created a discord bot using the discord.py libraries. This bot will be used in a private discord and will be improved upon as the needs of the private discord grow and and more complex functions are required and as my skills in the python coding language improve. This bot is a private applicatoin and will only be distributed to select discords servers. These commands are available to all users in the discord server and only when this bot is online. This bot will not be online all the time.

    All the functions that are used in this bot are imported from another python file called "bot_functions" and are referenced using bf.commandname

    This bot is also using @tree.command to set each command as a slash command accessible from discord chat

    The commands of this bot are:
    "/rolldice" - To be able to roll multiple types of dice a desired amount of times,
    "/help" - to be able to display to users all the commands this bot can take by using a help command,
    "/ping" - to be able to "ping-pong" with a user,
    "/morehelp" and able to go into detail of each command.

    #### "/help"
    When this command is typed into discord chat it will show a "slash" command and when entered, will display a code block that is a string that will contain a list of all the commmands available.

    Below is an how the @tree.commands are structured

    @tree.command(name="help", description="Displays some useful information about the bot", guild=MY_GUILD)

    "name='help'" is the name of the slash command
    "description='Displays some...'" is the description of the slash command that will appear under it
    "guild='MY_GUILD'" will assign the guild to the specified guild to ensure slash commands are updated quickly, rather than waiting up to one hour for the command to update

    #### "/ping"
    This is a simple command that when a user types "/ping" in the discord chat, Discourse Bot will return a message in the chat stating "Pong!"

    #### "/morehelp"
    This takes an additional option when using the slash command. The "command" option will take the user's input and when one of the other commands is input, it will run this command in a "check" command and then will use another function to return prompts based on the desired command.

    async def more_help_command(interaction: discord.Interaction, command: str):
    In this async def, "command" is labeled to accept only strings as an input.

    this references the "help_command_check_()" function which will return a boolean value to determine if a proper command was sent.

    #### "/rolldice"
    This is function will will take two options from the user. A dice type to roll, and how many times it will roll the dice.

    async def rolldice_command(interaction: discord.Interaction, dice: str, times: int):
    The option "dice" will accept only strings for the dice type
    The option "times" will accept only integers for the amount of times to roll that dice.

    This will call the "roll_dice_command_check(dice, time) function to ensure that a correct dice and a valid integer were input. Anything not in the defined dice types list will return False. Any integers that are "zero" or a negative integer will return False as well. This same function also limits the user to "20" dice rolls to prevent overloading the bot by checking if times > 20 and then will set time = 20 if input is greater than 20.

    If the function returns False, it will inform the user they have input an invalid dice type or roll amount.

    If the function returns True, it will call the "dice_roll(dice, times)" function and will return roll_results and roll_total.

    A message will be sent in the discord that contains a list of the rolls that were made and then will display the total of the rolls on the next line.
