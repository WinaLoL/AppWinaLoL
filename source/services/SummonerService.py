from source.services.RiotRequestService import RiotRequestService

import inject


class SummonerService:
    @inject.autoparams()
    def __init__(self, riot_request_service: RiotRequestService):
        self.riot_request_service = riot_request_service

    def get_summoner_puuid(self, summoner_name, tag_line):
        url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
        return self.riot_request_service.get(url)

