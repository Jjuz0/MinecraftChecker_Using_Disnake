import disnake
from disnake.ext import commands
class s(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.command()
    async def s(self, ctx):
        await ctx.send("⠀")
def setup(bot:commands.Bot):
    bot.add_cog(s(bot))
    print(f"{__name__} загружен.")
