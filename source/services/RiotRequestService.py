import requests
import inject

from source.services.EnvService import EnvService


class RiotRequestService:
    @inject.autoparams()
    def __init__(self, env_service: EnvService):
        self.riot_api_key = env_service.riot_api_key()

    def __get(self, url):
        url += f"?api_key={self.riot_api_key}"
        response = requests.get(url)

        return response.json()

    def get_summoner_puuid(self, name, tag):
        url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
        return self.__get(url)

    def get_summoner_encrypted_id(self, puuid):
        url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
        return self.__get(url)

