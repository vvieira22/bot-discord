from discord.ext import commands
import requests

# Cog subclasse de comandos

class Crypto(commands.Cog):
    """ Works with crypto currency"""
    def __init__(self, bot):
        self._bot = bot
    
    @commands.command()
    async def binance(self, ctx, coin, base):
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


def setup(bot):
    bot.add_cog(Crypto(bot))