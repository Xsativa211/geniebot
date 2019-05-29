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
    await client.change_presence(game=Game(name='Zeta Ragnarok Online : Gepard Shield',))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):  
    if message.author == client.user:
        return
    
    if message.content == '!invitation':
        await client.send_message(message.channel,'Official Discord Server Invitation Link https://discord.gg/AVznxUU')
    if message.content == '@request':
        await client.send_message(message.author,'@request is a command to send a Private Message from the staff in the game, please message us via Direct Message or Look for us in the game for your concerns.')     
      

client.run(str(os.environ.get('TOKEN')))
