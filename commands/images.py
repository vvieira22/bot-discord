from discord.ext import commands
import discord

# Cog subclasse de comandos

class Images(commands.Cog):
    """ Works with Images"""
    def __init__(self, bot):
        self._bot = bot

    @commands.command(name="foto")
    async def get_random_image(self, ctx):
        url_image = "https://picsum.photos/1920/1080"

        embed_image = discord.Embed(
            title = "Imagem aleatória:",
            description = "Exemplo de uso imagem aleatoria gostosinha",
            color = 0x2eff00,
        )

        embed_image.set_author(name=self._bot.user.name, icon_url=self._bot.user.avatar_url)
        embed_image.set_footer(text=f"Feito por:{self._bot.user.name}", icon_url=self._bot.user.avatar_url)

        embed_image.add_field(name="API", value="Usando api do https://picsum.photos")
        embed_image.add_field(name="Parâmetros", value="{largura}/{altura}")
        embed_image.add_field(name="Exemplo", value=url_image, inline=False)

        embed_image.set_image(url = url_image)

        await ctx.send(embed=embed_image)


def setup(bot):
    bot.add_cog(Images(bot))