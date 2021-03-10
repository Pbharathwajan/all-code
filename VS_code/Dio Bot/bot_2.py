import discord
import asyncio
from discord.ext import commands
from random import choice
import traceback

client = discord.Client()

@client.event
async def on_ready():
    print('KONO {0.user} DA!'.format(client))

@client.event
async def on_message(message):
    
    id = client.get_guild(723028897561837568)
    channels = ["general"]
    valid_users = [ "fastcandidate", "zyugyzarc", "Joel", "bonk"]
    cunts = ["bonk"]
    bad_words = ["bitch", "ass", "fuck", "shit", "penis", "zyugyzarc", "joel"]
    
    if str(message.channel) in channels and message.author.name in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
        if message.content.startswith("!add"):
            try:
                valid_users.append(message.mentions[0].name)
                await message.channel.send(f"added user {message.mentions[0].mention}.")
                print(valid_users)
            except IndexError:
                await message.channel.send('no member was tagged.')
        
        for word in bad_words:
            if message.content.count(word) > 0:
                await message.channel.purge(limit=1)
                await message.channel.send(f"{message.author.name} has said a bad word!")
                
                
                
        if message.content.startswith("!cunts"):
            try:
                cunts.append(message.mentions[0].name)
                await message.channel.send(f"added user {message.mentions[0].mention}.")
                print(cunts)
            except IndexError:
                await message.channel.send('no member was tagged.')
        
        
        if message.author.name in cunts:
            await message.channel.purge(limit=1)
            message.channel.send("Stupid cunt")
        
        

    
    
    if message.content.startswith('!DIO!'):
        await message.channel.send('https://www.youtube.com/watch?v=LjQZaD9EEJ0&list=PLVbxVQf7e2KRz1J34jFf7jDJFDT9lvnQ9&index=3')

    if message.content == "&stand":
        await message.channel.send(choice(open("/Users/Pachu/Documents/pachu/Coding/VS_code/Dio Bot/standnames.txt","r").read().split("\n"))) 

    if message.content.startswith('ping'):
        await message.channel.send('pong')

    if message.content.startswith('DIO!'):
        await message.channel.send("Oh? You're approaching me? Instead of running away you're coming right to me?")

    if message.content.startswith("I can't beat the shit out of you without getting closer."):
        await message.channel.send("HO HO, then get as close as you like.")
        await message.channel.send("https://cdn.discordapp.com/attachments/715251652323704860/762997548407324702/Approach.jpg")

    if message.content.startswith("ORA ORA ORA ORA ORA!"):
        await message.channel.send("MUDA MUDA MUDA MUDA MUDA!")
        await message.channel.send("https://cdn.discordapp.com/attachments/715251652323704860/762997641708830740/oraora.png")

    if message.content.startswith("tsk, DIO one thing's for sure, the next time I see your face my blood might burst."):
        await message.channel.send("ROAD ROLLER DA!")
        await message.channel.send("https://cdn.discordapp.com/attachments/715251652323704860/763037179231731742/roadroller.jpg")
        
    if message.content.startswith("ZA WARUDO TOKI YO TOMARE!"):
        await message.channel.send("Ichi byou keika")
        await asyncio.sleep(2)
        await message.channel.send("Ni byou keika")
        await asyncio.sleep(2)
        await message.channel.send("San byou keika")
        await asyncio.sleep(2)
        await message.channel.send("Yon byou keika")
        await asyncio.sleep(2)
        await message.channel.send("Go byou keika")
        await asyncio.sleep(2)
        await message.channel.send("Roku byou keika")
        await asyncio.sleep(2)
        await message.channel.send("Nana byou keika")
        await asyncio.sleep(2)
        await message.channel.send("Hachi byou keika")
        await asyncio.sleep(2)
        await message.channel.send("Kyu byou keika")
        await asyncio.sleep(2)
        await message.channel.send("ZA WARUDO Soshite toki ga ugokidesu!")
        

client.run('NzI0NjE4NzA0NTYxODk3NTEz.XvCzwQ.uXFmomsBCsY6tSr5um6QXzrwVZc')



