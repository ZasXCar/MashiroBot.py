import discord
import time
import asyncio

from discord.ext import commands
from index import config


class Script(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def recite(self, ctx, *, title: str):
        await ctx.send(f"Loading script '**{title}**'...\n")
        try:
            file = open(f"{title}.txt", "r")
            script = file.readlines()

            async with ctx.channel.typing():
                start = time.time()

                for line in script:
                    if line == '\n':
                        pass
                    else:
                        await asyncio.sleep(4)
                        await ctx.send(line)

                end = time.time()
                seconds = round(end - start)
                await ctx.send(f"\nDone! (Time elapsed: {seconds})")
        except FileNotFoundError:
            await ctx.send(f"Script named '**{title}**' cannot be found.")


def setup(client):
    client.add_cog(Script(client))
