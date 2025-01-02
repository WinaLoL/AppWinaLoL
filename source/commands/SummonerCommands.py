from discord.ext import commands

import inject
from source.services.SummonerService import SummonerService


class SummonerCommands(commands.Cog):
    @inject.autoparams()
    def __init__(self, summoner_service: SummonerService):
        self.summoner_service = summoner_service

    @commands.hybrid_command(name='add_summoner', description='Ajoute un ami à la liste des idiots.', with_app_command=True)
    async def add_summoner(self, ctx, summoner_name: str, tag_line: str):
        response = self.summoner_service.get_summoner_puuid(summoner_name, tag_line)
        await ctx.send(f"Add Summoner: {response}")

    @commands.hybrid_command(name='remove_summoner', description='Retire un ami de la liste des idiots.', with_app_command=True)
    async def remove_summoner(self, ctx):
        await ctx.send('Remove Summoner')

    @commands.hybrid_command(name='list_summoners', description='Affiche la liste actuelle des invocateurs.', with_app_command=True)
    async def list_summoners(self, ctx):
        await ctx.send('List Summoners')