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
    await client.change_presence(game=Game(name='Project ZetaRO',))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):  
    if message.content == "!official":
       await client.send_message(message.author, "Get the latest update and events from our Official ZetaRO Facebook Page and Group \n[Facebook Community Group]\nhttps://www.facebook.com/groups/315935882497689/\n[Facebook Page]\nhttps://www.facebook.com/Project-Zeta-911786119007085/ ")
    if ('!official') in message.content:
       await client.delete_message(message) 
    if message.content == '!invitation':
        await client.send_message(message.channel,'Official Discord Server Invitation Link https://discord.gg/AVznxUU')    
    if ('!official') in message.content:
       await client.delete_message(message) 
        
    if message.content.startswith('!update'):
        output = message.content.replace('!update ', '')
        await client.send_message(message.channel, 'Hello Zeta Players we have a new update! \n ' + output)
    if ('!br') in message.content:
       await client.delete_message(message)       
        
client.run(str(os.environ.get('TOKEN')))
