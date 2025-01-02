from source.entities.Summoner import Summoner
from source.repositories.SummonerRepository import SummonerRepository
from source.services.RiotRequestService import RiotRequestService

import inject


class SummonerService:
    @inject.autoparams()
    def __init__(self, riot_request_service: RiotRequestService, summoner_repository: SummonerRepository):
        self.riot_request_service = riot_request_service
        self.summoner_repository = summoner_repository

    def add_summoner(self, name, tag):
        puuid = self.riot_request_service.get_summoner_puuid(name, tag)['puuid']
        encrypted_id = self.riot_request_service.get_summoner(puuid)['id']

        summoner = Summoner(name, tag, puuid, encrypted_id)
        self.summoner_repository.add(summoner)

        return summoner

    def list_summoners(self):
        return self.summoner_repository.list()

    def remove_summoner(self, name, tag):
        summoner = self.summoner_repository.get(name, tag)
        self.summoner_repository.remove(summoner)

        return summoner



