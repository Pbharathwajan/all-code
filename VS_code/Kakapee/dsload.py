import discord

client = discord.Client()

@client.event
async def on_ready():
        
    try:

        channel = client.get_channel(749554487840079875)

        config  = open('config.json','r').read()
        await channel.send(config)
        print("found config.json, uploaded")


    except FileNotFoundError:
        
        m = await channel.history(limit =1).flatten()
        config = m[0].content
        print(f"File not found, found config.json as {config}")
        open('config.json','w').write(config)

    print('ignore incoming error:')
    exit()

try:
    client.run("NzIzMTY2MzUzMTEyMTcwNTc2.XutrJg.3vR5NjXXYEkrDJ8JPaEZKjaXdbc")
except KeyboardInterrupt:
    print("shutting down . . ")
