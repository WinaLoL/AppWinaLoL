from source.entities.Summoner import Summoner
from source.repositories.SummonerRepository import SummonerRepository
from source.services.RiotRequestService import RiotRequestService

import inject


class SummonerService:
    @inject.autoparams()
    def __init__(self, riot_request_service: RiotRequestService, summoner_repository: SummonerRepository):
        self.riot_request_service = riot_request_service
        self.summoner_repository = summoner_repository

    def add_summoner(self, name, line):
        puuid = self.riot_request_service.get_summoner_puuid(name, line)['puuid']

        summoner = Summoner(name, line, puuid)
        self.summoner_repository.add(summoner)

        return summoner

    def list_summoners(self):
        return self.summoner_repository.list()



