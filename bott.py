# import discord.py ALLOWS ACCESS TO DISCORD'S API

import discord
# Import the os module
import os

# import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# loads the dotenv file
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

# event listener for when the bot has switched from offline to online
@bot.event 
async def on_ready():
    guild_count = 0
    
# loop through all the server the bot is connected to 
for guild in bot.guilds:
    print(f"- {guild.id} (name: {guild.name})")
    
    guild_count = guild_count + 1
    
    print("Ai cub is in" + str(guild_count) + "guilds.")
    
# event listener for when a new message is sent to a channel.
@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("hi, welcome")
        
bot.run(DISCORD_TOKEN)  