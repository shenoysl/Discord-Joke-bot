# Discord bot that can sends various random jokes when you send a message with the command, !joke

import discord;
import requests;

TOKEN = "MTA3NDkwNTY4MjgzNjQ3NjAwNg.G-jqwz.ntoii5lYUiqqDcB2bwTzzA1guYsYoDQH-kBLiQ";

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("{0.user} now running!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("!joke"):
      r = requests.get('https://sv443.net/jokeapi/v2/joke/Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,racist,sexist&type=single').json()
      joke = r['joke']
      await message.channel.send(joke)

client.run(TOKEN);