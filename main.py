import inject
import asyncio
import discord
from discord.ext import commands

from source.services.ClassInjectorService import ClassInjectorService
from source.commands.UserCommands import UserCommands
from source.services.EnvService import EnvService

class Bot(commands.Bot):
    @inject.autoparams()
    def __init__(self, env_service: EnvService):
        self.token = env_service.token()

        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="??", intents=intents)

    def run(self):
        self.setup()
        super().run(self.token)

    def setup(self):
        cogs = [UserCommands]

        for cog in cogs:
            asyncio.run(self.add_cog(cog(self)))

    async def on_ready(self):
        print(f'Logged in as {self.user}')


if __name__ == '__main__':
    class_injector = ClassInjectorService()
    class_injector.inject()

    bot = Bot()
    bot.run()