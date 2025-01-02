from source.services.RiotRequestService import RiotRequestService
from source.services.RiotRessourceService import RiotRessourceService
import inject

class Summoner:
    name: str
    tag: str
    puuid: str

    def __init__(self, name: str, tag: str, puuid: str, encrypted_id: str):
        self.name = name
        self.tag = tag
        self.puuid = puuid
        self.encrypted_id = encrypted_id

    @property
    @inject.autoparams()
    def icon_url(self, riot_request_service: RiotRequestService, riot_resource_service: RiotRessourceService):
        summoner = riot_request_service.get_summoner(self.puuid)
        return riot_resource_service.get_icon_url(summoner['profileIconId'])

    def __str__(self):
        return f"{self.name}#{self.tag} ({self.puuid} - {self.encrypted_id})"
