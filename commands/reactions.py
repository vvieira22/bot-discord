from discord.ext import commands
from decouple import config

# Cog subclasse de comandos

class Talks(commands.Cog):
    """ Talk with user."""
    def __init__(self, bot):
        self._bot = bot

    # Reação na mensagem fixada no canal boe.
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👍":
            role = user.guild.get_role(int(config("CARGO_ULTRA_SECRETO")))
            await user.add_roles(role)

def setup(bot):
    bot.add_cog(Talks(bot))