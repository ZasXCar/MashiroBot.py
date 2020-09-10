import discord
import json

print("Loading...")


def read_token():
    with open("config.json", "r") as file:
        data = json.load(file)
        return data.get('token')


class MashiroBot(discord.Client):
    async def on_ready(self):
        TYELLOW = '\033[33m'
        ENDC = '\033[m'
        print(TYELLOW + str(self.user), ENDC, "has successfully loaded!")


client = MashiroBot()
token = read_token()
client.run(token)

# make a config file
