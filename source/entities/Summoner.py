class Summoner:
    name: str
    tag: str
    uuid: str

    def __init__(self, name: str, tag: str, uuid: str):
        self.name = name
        self.tag = tag
        self.uuid = uuid

    def __str__(self):
        return f"{self.name}#{self.tag} ({self.uuid})"
