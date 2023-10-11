# import discord.py ALLOWS ACCESS TO DISCORD'S API

import discord
# Import the os module
import os

# import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# loads the dotenv file

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
@client.event 
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
client.run(DISCORD_TOKEN)
