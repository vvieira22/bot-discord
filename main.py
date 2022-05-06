import discord
from discord.ext import commands, tasks
import re
import datetime

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print("estoy pronto")
    #so posso começar a task quando tiver pronto o bot.
    current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "cacete" in message.content:
        await message.channel.send(
            f"Pare de xingar {message.author.mention}!"
        ) 
    await bot.process_commands(message)

@bot.command(name="oi")
async def send_hello(ctx):
    user = ctx.author
    response = f'oi {user.mention}'
    await ctx.send(response)

@tasks.loop(seconds=5)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y ás %H:%M:%S")
    channel = bot.get_channel(971700495808876545)

    await channel.send("Data atual: " + now)

bot.run("OTY5NDExNzM5ODY5Mzg4ODMw.YmtBCQ.sxPdC-Z4ItyZZJFZlwpDCfztstc")


