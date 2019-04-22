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
    if message.author == client.user:
        return
    
    if message.content == "!official":
       await client.send_message(message.author, "Get the latest updates and events from our Official ZetaRO Facebook Page and Group \n[Facebook Community Group]\nhttps://www.facebook.com/groups/315935882497689/\n[Facebook Page]\nhttps://www.facebook.com/Project-Zeta-911786119007085/ ")
    if ('!official') in message.content:
       await client.delete_message(message) 
    if message.content == '!invitation':
        await client.send_message(message.channel,'Official Discord Server Invitation Link https://discord.gg/AVznxUU')
    if message.content == '@request':
        await client.send_message(message.author,'@request is a command to send a Private Message from the staff in the game, please use the #request channel on discord if you have a concern')     
        
    if ('!official') in message.content:
       await client.delete_message(message)
    if ('invitation') in message.content:
        await client.delete_message(message)     
        
    if message.content.startswith('!zbotupdate'):
        output = message.content.replace('!zbotupdate ', '')
        await client.send_message(message.channel, 'Hello Zeta Players we have a new update! \n ' + output)
    if ('!zbotupdate') in message.content:
       await client.delete_message(message)      
    
    
    if message.content.startswith('!helper'):
        for user in message.mentions:
            msg = ' Hello {} If you have a question look for people who have the role "Support Team" or user with the violet name\nThey can help you regarding on your concerns and questions! or leave us a message at #request channel '.format(user.mention)
            await client.send_message(message.channel, msg)            
    if ('!helper') in message.content:
       await client.delete_message(message)


    if message.content == '!hbctam':
        await client.send_message(message.channel,'Hello <@!285843163585839107> is currently active in game and discord!\nSend her a message if you have a questions\n```Her In Game Name Helper is <your in game name>```')    
    if ('!hbctam') in message.content:
        await client.delete_message(message)
    if message.content == '!hbcjoe':
        await client.send_message(message.channel,'Hello <@!324825272916639744> is currently active in game and discord!\nSend her a message if you have a questions\n```Her In Game Name Helper is <your in game name>```')    
    if ('!hbcjoe') in message.content:
        await client.delete_message(message)  

    
    if message.content.startswith("!zhelp"):
        em = discord.Embed(title="Zeta Bot Commands", description="Show you the bot commands available for you!", colour=0xcc780a)
        em.set_thumbnail(url=message.server.icon_url)
        em.set_author(name= message.author.nick)
        em.add_field(name="!official", value="Gives you the official link Facebook Page and Community Group.", inline=False)
        em.add_field(name="!invite", value="Gives you the Discord Server invitation.", inline=False)
        em.add_field(name="!guide", value="To Be Announce!", inline=False)
        em.add_field(name="@request", value="Send you the usage of the command", inline=False)        
        em.add_field(name="!forums", value="Link to be updated soon!", inline=False)
        em.set_footer(text="Server Discord and Bot Owner Jhake#4303")
        await client.send_message(message.channel, embed=em)    
        
client.run(str(os.environ.get('TOKEN')))
