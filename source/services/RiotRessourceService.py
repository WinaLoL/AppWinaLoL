import requests

class RiotRessourceService:
    def __get_latest_version(self):
        url = f"https://ddragon.leagueoflegends.com/api/versions.json"
        response = requests.get(url)

        return response.json()[0]

    def get_icon_url(self, id):
        latest_version = self.__get_latest_version()

        return f"http://ddragon.leagueoflegends.com/cdn/{latest_version}/img/profileicon/{id}.png"


