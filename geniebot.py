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
    await client.change_presence(game=Game(name='SOAR',))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):
    if message.content == '!link':
       await client.send_message(message.channel,'Discord Invitation link\nhttps://discord.me/genocideguild')

### Auto Delete Message Section ###
    if ('!daily') in message.content:
       await client.delete_message(message)
    if ('!daily2') in message.content:
       await client.delete_message(message)    
    
    
### channel Message ###
    if message.content.startswith("!daily"):
        em = discord.Embed(title="SOAR Daily Link", description="Can View the daily linked used when voting", colour=0xcc780a)
        em.set_thumbnail(url=message.server.icon_url)
        em.set_author(name= message.author.nick)
        em.add_field(name="Submisstion Form", value="https://bit.ly/2wAP1rb", inline=False)
        em.add_field(name="Check if your account is Shadowbanned or Suspended", value="https://bit.ly/2UCyPxw", inline=False)
        em.add_field(name="View Everyones Earnings", value="https://bit.ly/2UwqZFI", inline=False)
        em.set_footer(text="Content Create By: SOAR Staff Team")
        await client.send_message(message.channel, embed=em)
        
### Discord Direct Message ###
    if message.content.startswith("!daily2"):
        em = discord.Embed(title="SOAR Daily Link", description="Can View the daily linked used when voting", colour=0xcc780a)
        em.set_thumbnail(url=message.server.icon_url)
        em.set_author(name= message.author.nick)
        em.add_field(name="Submisstion Form", value="https://bit.ly/2wAP1rb", inline=False)
        em.add_field(name="Check if your account is Shadowbanned or Suspended", value="https://bit.ly/2UCyPxw", inline=False)
        em.add_field(name="View Everyones Earnings", value="https://bit.ly/2UwqZFI", inline=False)
        em.set_footer(text="Content Create By: SOAR Staff Team")
        await client.send_message(message.author, embed=em)        
    
client.run(str(os.environ.get('TOKEN')))
