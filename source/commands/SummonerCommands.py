from discord.ext import commands

import inject
from source.services.SummonerService import SummonerService


class SummonerCommands(commands.Cog):
    @inject.autoparams()
    def __init__(self, summoner_service: SummonerService):
        self.summoner_service = summoner_service

    @commands.hybrid_command(name='add_summoner', description='Ajoute un ami à la liste des idiots.', with_app_command=True)
    async def add_summoner(self, ctx, name: str, tag: str):
        self.summoner_service.add_summoner(name, tag)

        await ctx.send(f"Ajout de {name}#{tag} à la liste des invocateurs.")

    @commands.hybrid_command(name='remove_summoner', description='Retire un ami de la liste des idiots.', with_app_command=True)
    async def remove_summoner(self, ctx):
        await ctx.send('Remove Summoner')

    @commands.hybrid_command(name='list_summoners', description='Affiche la liste actuelle des invocateurs.', with_app_command=True)
    async def list_summoners(self, ctx):
        summoners = self.summoner_service.list_summoners()

        await ctx.send(f"List Summoners: {', '.join([str(summoner) for summoner in summoners])}")