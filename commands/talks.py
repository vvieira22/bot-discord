from discord.ext import commands

# Cog subclasse de comandos

class Talks(commands.Cog):
    """ Talk with user."""
    def __init__(self, bot):
        self._bot = bot

    #bot.command => commands.command
    @commands.command(name="oi")
    async def send_hello(self, ctx):
        user = ctx.author
        response = f'oi {user.mention}'
        await ctx.send(response)

    #qualquer pessoa mandando msg em canal publico mas o bot responde no privado.
    @commands.command(name="segredinho", help="Não requer argumento, apenas os espertos usam esse comando.")
    async def secret(self, ctx):
        await ctx.author.send(f'{ctx.author.mention}, você é gostoso(a) 🥵')

def setup(bot):
    bot.add_cog(Talks(bot))