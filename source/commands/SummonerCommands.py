import discord
import inject

from discord.ext import commands
from source.services.SummonerService import SummonerService


class SummonerCommands(commands.Cog):
    @inject.autoparams()
    def __init__(self, summoner_service: SummonerService):
        self.summoner_service = summoner_service

    @commands.hybrid_command(name='add_summoner', description='Ajoute un ami à la liste des idiots.', with_app_command=True)
    async def add_summoner(self, ctx, name: str, tag: str):
        summoner = self.summoner_service.add_summoner(name, tag)

        embed = discord.Embed(
            title="Invocateur ajouté",
            description=f"{summoner.name}#{summoner.tag} a été ajouté à la liste des invocateurs par {ctx.author.mention}.",
        )
        embed.set_thumbnail(url=summoner.icon_url)

        await ctx.send(embed=embed)

    @commands.hybrid_command(name='remove_summoner', description='Retire un ami de la liste des idiots.', with_app_command=True)
    async def remove_summoner(self, ctx):
        await ctx.send('Remove Summoner')

    @commands.hybrid_command(name='list_summoners', description='Affiche la liste actuelle des invocateurs.', with_app_command=True)
    async def list_summoners(self, ctx):
        summoners = self.summoner_service.list_summoners()

        await ctx.send(f"List Summoners: {', '.join([str(summoner) for summoner in summoners])}")