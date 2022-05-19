from discord.ext import commands, tasks
import datetime

# Cog subclasse de comandos

class Dates(commands.Cog):
    """ Works with dates"""
    def __init__(self, bot):
        self._bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(seconds=100)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y ás %H:%M:%S")
        channel = self._bot.get_channel(971700495808876545)

        await channel.send("Data atual: " + now)


def setup(bot):
    bot.add_cog(Dates(bot))