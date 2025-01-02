import inject
import discord
from discord.ext import commands

from source.commands.TestCommands import TestCommand
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
        super().run(self.token)

    async def setup_cog(self):
        cogs = [UserCommands, TestCommand]

        for cog in cogs:
            await self.add_cog(cog(self))

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def setup_hook(self):
        await self.setup_cog()
        self.tree.clear_commands(guild=discord.Object(id=1163969445388111932))
        self.tree.copy_global_to(guild=discord.Object(id=1163969445388111932))
        await self.tree.sync(guild=discord.Object(id=1163969445388111932))

if __name__ == '__main__':
    class_injector = ClassInjectorService()
    class_injector.inject()

    bot = Bot()
    bot.run()