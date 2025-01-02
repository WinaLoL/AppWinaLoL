import inject

from source.repositories.SummonerRepository import SummonerRepository
from source.services.EnvService import EnvService
from source.services.RiotRequestService import RiotRequestService
from source.services.RiotRessourceService import RiotRessourceService
from source.services.SummonerService import SummonerService


class ClassInjectorService:
    def inject(self):
        inject.configure(self.configure)

    @staticmethod
    def configure(binder):
        #Repositories
        summoner_repository = SummonerRepository()

        #Services
        env_service = EnvService()
        riot_request_service = RiotRequestService(env_service)
        riot_resource_service = RiotRessourceService()
        summoner_service = SummonerService(riot_request_service, summoner_repository)

        binder.bind(EnvService, env_service)
        binder.bind(RiotRequestService, riot_request_service)
        binder.bind(RiotRessourceService, riot_resource_service)
        binder.bind(SummonerService, summoner_service)
