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
### Auto Delete Message Section ###
    if ('!official') in message.content:
       await client.delete_message(message)
    if ('!invitation') in message.content:
        await client.delete_message(message)
    if ('!mainhall') in message.content:
        await client.delete_message(message)
    if ('!zetahelp') in message.content:
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
        await client.send_message(message.channel,'Hello <@!285843163585839107> is currently active in game and discord!\nSend her a message if you have a questions\n```Her In Game Name  is Tofu```')    
    if ('!hbctam') in message.content:
        await client.delete_message(message)
    if message.content == '!hbcvox':
        await client.send_message(message.channel,'Hello <@!324825272916639744> is currently active in game and discord!\nSend him a message if you have a questions\n```His In Game Name is Vox Populi```')    
    if ('!hbcvox') in message.content:
        await client.delete_message(message)  

### DISCORD COMMANDS ###    
    if message.content.startswith("!zetahelp"):
        em = discord.Embed(title="Zeta Bot Commands", description="Show you the bot commands available for you!", colour=0xcc780a)
        em.set_thumbnail(url=message.server.icon_url)
        em.set_author(name= message.author.nick)
        em.add_field(name="!official", value="Gives you the official link of ZetaRO Forums,Website,Facebook Page & Group", inline=False)
        em.add_field(name="!invitation", value="Instantly give you discord invitation", inline=False)
        em.add_field(name="!guide", value="To Be Announce!", inline=False)
        em.add_field(name="@request", value="Send you the usage of the command", inline=False)        
        em.set_footer(text="Server Discord and Bot Owner Jhake#4303")
        await client.send_message(message.channel, embed=em)    
### MAIN HALL ###
    if message.content.startswith("!mainhall"):
        em = discord.Embed(title="Prontera Main Hall Building", description="@warp prontera 167 167", colour=0xcc780a)
        em.set_thumbnail(url=message.server.icon_url)
        em.set_author(name= message.author.nick)
        em.add_field(name="Daily Rewards & Hourly Rewards NPCs", value="@warp prt_in 248 163", inline=False)
        em.add_field(name="Dressing Coach and Costume Maker", value="@warp prt_in 284 131", inline=False)
        em.add_field(name="Voting Staff and Activity Shop NPC", value="@warp prt_in 281 168", inline=False)
        em.set_footer(text="Content Create By: Staff Team & Discord,Ragnarok Server Owner Jhake#4303")
        await client.send_message(message.author, embed=em)
### Forum | Panel | Facebook Page and Group Link ###
    if message.content.startswith("!official"):
        em = discord.Embed(title="ZetaRO Official Links", description="Forum | Panel | Facebook Page and Group Link", colour=0xcc780a)
        em.set_thumbnail(url=message.server.icon_url)
        em.set_author(name= message.author.nick)
        em.add_field(name="Facebook Group", value="https://www.facebook.com/groups/315935882497689/", inline=False)
        em.add_field(name="Facebook Page", value="https://web.facebook.com/Project-Zeta-911786119007085/", inline=False)
        em.add_field(name="ZetaRO Community Forum", value="http://zeta-ro.com/forum/", inline=False)
        em.add_field(name="ZetaRO Website", value="http://zeta-ro.com/panel/", inline=False)
        em.add_field(name="Server Information", value="http://zeta-ro.com/panel/?module=pages&action=server_info", inline=False)
        em.set_footer(text="Content Create By: Staff Team & Discord,Ragnarok Server Owner Jhake#4303")
        await client.send_message(message.author, embed=em)         

client.run(str(os.environ.get('TOKEN')))
