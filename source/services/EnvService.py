import os

from dotenv import load_dotenv

class EnvService:
    def __init__(self):
        load_dotenv()

    def token(self):
        return os.getenv("TOKEN")

    def riot_api_key(self):
        return os.getenv("RIOT_API_KEY")