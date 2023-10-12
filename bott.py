  # Import the os module that the functions interacts with the operating system
import os

# import discord.py ALLOWS ACCESS TO DISCORD'S API
import discord

# import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# loads the dotenv file

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

bot = discord.Client(intents='')

@bot.event 
async def on_ready():
    for guild in bot.guilds:
        if guild.name == DISCORD_GUILD:
            break 
        
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
        )
             
bot.run(DISCORD_TOKEN)
