import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import requests
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='PeenoiseSync', type = 2))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):
    if message.content == 'genie':
        await client.send_message(message.channel,'Hehehe busy po leave message nalang')
    if ('genie') in message.content:
       await client.delete_message(message)
    if message.content == 'Genie':
        await client.send_message(message.channel,'Hehehe busy po leave message nalang')
    if ('Genie') in message.content:
       await client.delete_message(message)
    if message.content == 'tammy':
        await client.send_message(message.channel,'Hehehe busy po leave message nalang')
    if ('tammy') in message.content:
       await client.delete_message(message)    
    if message.content == 'Tammy':
        await client.send_message(message.channel,'Hehehe busy po leave message nalang')
    if ('Tammy') in message.content:
       await client.delete_message(message)
    if message.content == "!botcheck":
       await client.send_message(message.author, "I am active :)")    

    if message.content.startswith('!br'):
        output = message.content.replace('!br ', '')
        await client.send_message(message.channel, 'Hello! Everyone we have new Server Update! \n ' + output)
    if ('!br') in message.content:
       await client.delete_message(message)
    
    if message.content.startswith('!bc'):
        output = message.content.replace('!bc ', '')
        await client.send_message(message.channel, 'OYOYOYOYOYOY ' + output)
    if ('!bc') in message.content:
       await client.delete_message(message)     
        
client.run(str(os.environ.get('TOKEN')))
