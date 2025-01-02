from discord.ext import commands

class TestCommands(commands.Cog):
    @commands.hybrid_command(name='ping', description='Commande de test', with_app_command=True)
    async def test(self, ctx):
        await ctx.send('Pong!')