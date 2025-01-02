class SummonerRepository:
    def __init__(self):
        self.summoners = []

    def add(self, summoner):
        self.summoners.append(summoner)

    def list(self):
        return self.summoners