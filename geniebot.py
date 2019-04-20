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
    await client.change_presence(game=Game(name='Project Zeta',))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):
    if message.content == '!zeta':
        await client.send_message(author,'Hello! Welcome to Zeta Ragnarok Online')
    if message.content == '!test':
        await client.send_message(message.channel,'Hello this is just a test from zetaRO')
    if ('!test') in message.content:
       await client.delete_message(message)     

    if message.content.startswith('!br'):
        output = message.content.replace('!br ', '')
        await client.send_message(message.channel, 'Hello Everyone! Everyone we have new Server Update! \n ' + output)
    if ('!br') in message.content:
       await client.delete_message(message)
    
    if message.content.startswith('!bc'):
        output = message.content.replace('!bc ', '')
        await client.send_message(message.channel, 'Greetings Players! we have new discord server update ' + output)
    if ('!bc') in message.content:
       await client.delete_message(message)     
        
client.run(str(os.environ.get('TOKEN')))
