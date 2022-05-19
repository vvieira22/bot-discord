from discord.ext import commands

# Cog subclasse de comandos

class Calc(commands.Cog):
    """ Calc"""
    def __init__(self, bot):
        self._bot = bot

    @commands.command(name="calcular")
    async def calculate_expression(self, ctx, *expression):
        print(expression)
        expression = "".join(expression)
        print(expression)

        response = eval(expression)
        
        await ctx.send("A resposta é: "+ str(response))

def setup(bot):
    bot.add_cog(Calc(bot))