from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
import datetime
import discord

# Cog subclasse de comandos

class Manager(commands.Cog):
    """ Manage the bot """
    def __init__(self, bot):
        self._bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("estoy pronto")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Você precisa enviar todos argumentos.\nDigite !help {comando} para ver os argumentos de cada comando.!")
        elif isinstance(error, CommandNotFound):
            await ctx.send("Comando " + '{'+ctx.message.content+'}' + " encontrado :(\nDigite !help {comando} para ver todos os comandos !")
        else:
            raise error

    #event => @commands.Cog.listener()
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self._bot.user:
            return
        if "cacete" in message.content:
            await message.channel.send(
                f"Para de xingar {message.author.mention}!"
            ) 
        #so vai funcionar se mandar msg no privado e for vitor
        if isinstance(message.channel, discord.channel.DMChannel):
            if "configuracoes" in message.content and message.author.id == 277607401069477888:
                await message.channel.send('mensagem apenas para vitor no privado')

def setup(bot):
    bot.add_cog(Manager(bot))