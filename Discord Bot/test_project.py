from bot_functions import more_help_command_check
from bot_functions import more_help_prompts
from bot_functions import dice_roll

def main():
    test_more_help()
    test_help_prompts()
    test_dice_roll()

def test_more_help():
    assert more_help_command_check("rolldice") == True
    assert more_help_command_check("duck") == False

def test_help_prompts():
    assert more_help_prompts("rolldice") == """With this commmand you can roll a dice up to `20` times. Below are the types of dice that you can roll
- D4
- D8
- D12
- D20
- D100
"""
    assert more_help_prompts("chicken") == False

def test_dice_roll():
    assert dice_roll("d4", 1) == ([1], 1) or ([2], 1) or ([3], 1) or ([4], 1)
    assert dice_roll("d4", 1) != ([5], 2)
if __name__ == "__main__":
    main()
