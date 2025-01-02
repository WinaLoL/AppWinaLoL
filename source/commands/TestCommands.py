from discord.ext import commands

class TestCommand(commands.Cog):
    @commands.hybrid_command(name='ping', description='Test command', with_app_command=True)
    async def test(self, ctx):
        await ctx.send('Pong!')