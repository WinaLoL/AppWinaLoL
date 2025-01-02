class SummonerRepository:
    def __init__(self):
        self.summoners = []

    def add(self, summoner):
        self.summoners.append(summoner)

    def remove(self, summoner):
        self.summoners.remove(summoner)

    def get(self, name, tag):
        for summoner in self.summoners:
            if summoner.name == name and summoner.tag == tag:
                return summoner
        return None

    def list(self):
        return self.summoners