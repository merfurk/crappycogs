from redbot.core import commands

class Tinycreep(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go heree
        await ctx.send("Hello World!")
