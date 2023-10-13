  # Import the os module that the functions interacts with the operating system
import os

# import discord.py ALLOWS ACCESS TO DISCORD'S API
import discord

# import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# loads the dotenv file

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient (discord.Client): 
 async def on_ready(self):
    print(f'logged on as {self.user}')
  
async def on_message(self, message):
  print(f'Message from {message.auth}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)

#interaction
