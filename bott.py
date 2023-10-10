# import discord.py ALLOWS ACCESS TO DISCORD'S API

import discord
# Import the os module
import os

# import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# loads the dotenv file
# import commands from the discord.ext module.
from discord.ext import commands
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.intents.default()

# creates a new bot object with a specified prefix.
bot = commands.Bot(command_prefix="$", intents=intents)
    
# on_message() event listener.
@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("hi, welcome to the AI server")
        
    await bot.process_commands(message)
    
@bot.command(name = "ping")

async def ping(ctx):
    await ctx.channel.send("pong")
    
@bot.command (name="ping")

async def print(ctx, *args):
    response = ""
    
    for arg in args:
        response = response + " " + arg 
        
    await ctx.channel.send(response)

bot.run(DISCORD_TOKEN)
