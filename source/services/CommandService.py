from discord.ext import commands

from source.services.UserService import UserService

class CommandService:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def add_commands(self):
        @self.bot.command(name='hello')
        async def hello(ctx):
            user_service = UserService(ctx)
            await user_service.hello_sender()