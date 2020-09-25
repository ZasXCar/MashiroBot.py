import discord
import json
import random
from discord.ext import commands


class BasicCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("MashiroBot is online.")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        await ctx.send(f'`{left} + {right} = {left + right}`')

    @commands.command(aliases=['8ball'])
    async def ask(self, ctx, *, question=None):
        file = open("botdata.json", "r")
        intents = json.load(file)
        if question is None:
            await ctx.send(f'{random.choice(intents["blank"])}')
        else:
            await ctx.send(f'{random.choice(intents["responses"])}')


def setup(client):
    client.add_cog(BasicCommands(client))

