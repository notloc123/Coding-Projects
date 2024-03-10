import discord
from discord import app_commands
from dotenv import load_dotenv, dotenv_values
import os
import bot_functions

load_dotenv()
config = dotenv_values(".env")
intents = discord.Intents.all()
TOKEN = os.getenv("TOKEN")
MY_GUILD = discord.Object(id=1180303769200754709)
bf = bot_functions


class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=MY_GUILD)
        self.synced = True
        print(f"{self.user} is now running!")

client = Client()
tree = app_commands.CommandTree(client)

@tree.command(name="help", description="Displays some useful information about the bot", guild=MY_GUILD)
async def help(interaction: discord.Interaction):
  await interaction.response.send_message(f"""```Hello! Here are some of my commands!

- ping
- rolldice

If you have questions about a specifc command, please type '/morehelp [commandname]' for more details about what that command will do```""")


@tree.command(name="morehelp", description="Will provide more details on a commands", guild=MY_GUILD)
async def more_help_command(interaction: discord.Interaction, command: str):
    help_command_check_result = bf.more_help_command_check(command)
    if help_command_check_result == True:
        await interaction.response.send_message(bot_functions.more_help_prompts(command))
    else:
        await interaction.response.send_message("Please enter a valid command. You can type `/help` for a list of working commands")

@tree.command(name="ping", description="Will pong the user's ping", guild=MY_GUILD)
async def ping_command(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@tree.command(name="rolldice", description="Will roll a dice of the selected type", guild=MY_GUILD)
async def rolldice_command(interaction: discord.Interaction, dice: str, times: int):
    if times > 20:
        times = 20
    roll_dice_check_result = bf.roll_dice_command_check(dice, times)
    if roll_dice_check_result == True:
        roll_results, roll_total_results = bf.dice_roll(dice, times)
        await interaction.response.send_message(f"You rolled a `{dice.upper()}`, `{times}` times\nRolls: {roll_results}\nTotal: {roll_total_results}")
    else:
        await interaction.response.send_message(f"""Invalid dice type or roll amount.
Please type `/morehelp rolldice` for additional information about this command""")


def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()
