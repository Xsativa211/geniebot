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
    await client.change_presence(game=Game(name='Soar',))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):  
    if message.author == client.user:
        return
### Auto Delete Message Section ###
    if ('!here') in message.content:
       await client.delete_message(message)      
    if ('!sipon') in message.content:
       await client.delete_message(message)  
    if ('!help') in message.content:
       await client.delete_message(message)     
    
        
    if message.content.startswith('!here'):
        output = message.content.replace('!here ', '')
        await client.send_message(message.channel, 'Hello Everyone We Have an Announcement! \n ' + output)
    if ('!here') in message.content:
       await client.delete_message(message)      
      
    if message.content.startswith('!helper'):
        for user in message.mentions:
            msg = ' Hello {} If you have a question look for people who have the role "Support Team" or user with the violet name\nThey can help you regarding on your concerns and questions! or leave us a message at #request channel '.format(user.mention)
            await client.send_message(message.channel, msg)            
    if ('!helper') in message.content:
       await client.delete_message(message)

    if message.content == '!sipon':
        await client.send_message(message.channel,'Hello <@!285843163585839107> is currently offline!\nHe will check your message once he gets baack on!')    
    if ('!hbctam') in message.content:
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
        
### SOAR Main Links ###
    if message.content.startswith("!help"):
        em = discord.Embed(title="Prontera Main Hall Building", description="@warp prontera 167 167", colour=0xcc780a)
        em.set_thumbnail(url=message.server.icon_url)
        em.set_author(name= message.author.nick)
        em.add_field(name="Submission Form", value="https://docs.google.com/forms/d/e/1FAIpQLSeGdlxg5wUY5BfaZk4MlSN6uz76WIwckwh9A1SBTuV__VOxxA/viewform?pli=1", inline=False)
        em.add_field(name="To Check Your Reddit Status", value="https://nullprogram.com/am-i-shadowbanned/?#magboul2331", inline=False)
        em.add_field(name="View Your Earnings", value="https://docs.google.com/spreadsheets/d/1tkPDblhdd9DC3PfdcoI9ZmQzcXdOuV-_5_uzUcvq4VA/edit#gid=0", inline=False)
        em.set_footer(text="Content Create By: Soar Staff Team!")
        await client.send_message(message.author, embed=em)
             
    if message.content == '!invitation':
        await client.send_message(message.channel,'Official Discord Server Invitation Link https://discord.gg/AVznxUU')
    if message.content == '@request':
        await client.send_message(message.author,'@request is a command to send a Private Message from the staff in the game, please message us via #support or Look for us in the game for your concerns.')     
   

client.run(str(os.environ.get('TOKEN')))
