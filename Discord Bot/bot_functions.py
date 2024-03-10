import random

def more_help_command_check(command):
    commands = ['rolldice', 'help']
    if command.lower() in commands:
        return True
    else:
        return False

def more_help_prompts(command):
    if command == "rolldice":
        return rolldiceprompt()
    if command == "help":
        return helpprompt()
    else:
        return False

def roll_dice_command_check(dice, times):
    types = ["d3","d4","d6", "d8", "d12", "d20", "d100"]
    if dice in types and times > 0:
        return True
    else:
        return False


def dice_roll(dice, times):
    types = ["d3", "d4","d6", "d8", "d12", "d20", "d100"]
    rolls = []
    total = 0
    if times > 20:
        times = 20
    while total <= 20:
        try:
            if dice.lower() in types:
                dice = int(dice.strip("d"))
                for _ in range(times):
                    result = random.randint(1, dice)
                    print(f"Roll: {result}")
                    rolls.append(result)
                    total += result
                print(f"Total: {total}")
                return rolls, total
            else:
                raise ValueError
        except ValueError:
            result = "Invalid dice or roll input"
            return result

def rolldiceprompt():
    return """With this commmand you can roll a dice up to `20` times. Below are the types of dice that you can roll
- D3
- D4
- D6
- D8
- D12
- D20
- D100
"""

def helpprompt():
    return """You can type this in to get an idea of some commands that I am capable of."""
