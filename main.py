from pydoc import describe
import discord
from discord.ext import commands, tasks
import re
from decouple import config
import os

bot = commands.Bot("!")

def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("tasks.dates")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)
lista_comandos = []

for command in bot.commands:
	lista_comandos.append(str(command))

LISTA_COMANDOS = lista_comandos
print(LISTA_COMANDOS)
TOKEN = config("TOKEN_DISCORD")
bot.run(TOKEN)
