import discord
import os
from dotenv import load_dotenv
import random

load_dotenv()

intents = discord.Intents.default()
# allowing sending message to group:
intents.message_content = True

client = discord.Client(intents=intents)

rps = ['rock', 'paper', 'scissor']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('echo '):
        # deleting user's message:
        await message.delete()
        await message.channel.send(f'{message.author} said: "{message.content[5:]}"'.format(message))
    if message.content == "$rock" or message.content == "$paper" or message.content == "$scissor":
        chosen_rps = rps[random.randint(0, 2)]
        await message.channel.send(f"I choose {chosen_rps}".format(message))
        if chosen_rps == message.content[1:]:
            await message.channel.send(f"draw".format(message))
        elif chosen_rps == 'rock' and message.content[1:] == 'paper':
            await message.channel.send(f"you win".format(message))
        elif chosen_rps == 'paper' and message.content[1:] == 'scissor':
            await message.channel.send(f"you win".format(message))
        elif chosen_rps == 'scissor' and message.content[1:] == 'rock':
            await message.channel.send(f"you win".format(message))
        else:
            await message.channel.send(f"you lose".format(message))


client.run(os.getenv('TOKEN'))