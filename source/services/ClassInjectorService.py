import inject

from source.services.EnvService import EnvService
from source.services.RiotRequestService import RiotRequestService
from source.services.SummonerService import SummonerService


class ClassInjectorService:
    def inject(self):
        inject.configure(self.configure)

    @staticmethod
    def configure(binder):
        env_service = EnvService()
        riot_request_service = RiotRequestService(env_service)
        summoner_service = SummonerService(riot_request_service)

        binder.bind(EnvService, env_service)
        binder.bind(RiotRequestService, riot_request_service)
        binder.bind(SummonerService, summoner_service)
