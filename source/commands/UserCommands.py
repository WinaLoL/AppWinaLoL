from discord.ext import commands


class UserCommands(commands.Cog):

    @commands.hybrid_command(name='hello', description='Say Hello to sender', with_app_command=True)
    async def hello(self, ctx):
        sender_username = ctx.author.name
        await ctx.send(f'Hello, {sender_username}!')