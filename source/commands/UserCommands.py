from discord.ext import commands

class UserCommands(commands.Cog):

    @commands.command(name='hello')
    async def hello(self, ctx):
        sender_username = ctx.author.name
        await ctx.send(f'Hello, {sender_username}!')