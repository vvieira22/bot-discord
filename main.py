import discord
from discord.ext import commands, tasks
import re
import datetime
import requests

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print("estoy pronto")
    #so posso começar a task quando tiver pronto o bot.
    current_time.start()

@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):
    print(expression)
    expression = "".join(expression)
    print(expression)

    response = eval(expression)
    
    await ctx.send("A resposta é: "+ str(response))

@bot.command()
async def binance(ctx, coin, base):
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
        
        data = response.json()
        price = data.get("price")
        if price:    
            await ctx.send(f"o Valor do {coin}/{base} é {price}")
        else:
            await ctx.send(f"o par do {coin}/{base} é inválido")
    except Exception as e:
        await ctx.send("Ops... algo deu errado, verifique o comando novamente")
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "cacete" in message.content:
        await message.channel.send(
            f"Para de xingar {message.author.mention}!"
        ) 
    #so vai funcionar se mandar msg no privado e for vitor
    if isinstance(message.channel, discord.channel.DMChannel):
        if "configuracoes" in message.content and message.author.id == 277607401069477888:
            await message.channel.send('mensagem apenas para vitor no privado')
    await bot.process_commands(message)

#qualquer pessoa mandando msg em canal publico mas o bot responde no privado.
@bot.command(name="segredinho")
async def secret(ctx):
    await ctx.author.send("hehe, muito bom garotinho.")

@bot.command(name=" ")
async def send_hello(ctx):
    user = ctx.author
    response = f'oi {user.mention}'
    await ctx.send(response)

@tasks.loop(seconds=100)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y ás %H:%M:%S")
    channel = bot.get_channel(971700495808876545)

    await channel.send("Data atual: " + now)

bot.run("OTY5NDExNzM5ODY5Mzg4ODMw.YmtBCQ.btyP2NVcjyRM-QG82MFs8gBOlXY")


