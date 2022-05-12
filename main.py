from pydoc import describe
import discord
from discord.ext import commands, tasks
import re
import datetime
import requests
import config_token
from discord.ext.commands import CommandNotFound
import roles

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

@bot.command(name="oi")
async def send_hello(ctx):
    user = ctx.author
    response = f'oi {user.mention}'
    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"Comando {ctx.message.content} não encontrado :(")

@tasks.loop(seconds=100)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y ás %H:%M:%S")
    channel = bot.get_channel(971700495808876545)

    await channel.send("Data atual: " + now)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "👍":
        role = user.guild.get_role(roles.CARGO_ULTRA_SECRETO)
        await user.add_roles(role)

@bot.command(name="foto")
async def get_random_image(ctx):
    url_image = "https://picsum.photos/1920/1080"

    embed_image = discord.Embed(
        title = "Imagem aleatória:",
        description = "Exemplo de uso imagem aleatoria gostosinha",
        color = 0x2eff00,
    )

    embed_image.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_image.set_footer(text=f"Feito por:{bot.user.name}", icon_url=bot.user.avatar_url)

    embed_image.add_field(name="API", value="Usando api do https://picsum.photos")
    embed_image.add_field(name="Parâmetros", value="{largura}/{altura}")
    embed_image.add_field(name="Exemplo", value=url_image, inline=False)

    embed_image.set_image(url = url_image)

    await ctx.send(embed=embed_image)

bot.run(config_token.retornar_token())


