import requests
import inject

from source.services.EnvService import EnvService


class RiotRequestService:
    @inject.autoparams()
    def __init__(self, env_service: EnvService):
        self.riot_api_key = env_service.riot_api_key()

    def get(self, url):
        url += f"?api_key={self.riot_api_key}"
        response = requests.get(url)
        
        return response.json()