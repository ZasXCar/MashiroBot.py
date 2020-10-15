import discord
import nhentai
import time

from discord.ext import commands
from index import config


class NHentai(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10.0)
    async def decode(self, ctx, sauce=None):
        if sauce is None:
            await ctx.send('Please enter the sauce first: \n'
                           f'```{config["PREFIX"]}decode <sauce>```')
        else:
            try:
                ctx.send("Decoding sauce...")
                start = time.time()
                hentai = nhentai.get_doujin(int(sauce))
                cover = hentai.cover
                english_title = hentai.titles.get("english")
                japanese_title = hentai.titles.get("japanese")
                pages = str(len(hentai.pages))
                link = "||https://nhentai.net/g/" + sauce + "||"
                tags = [getattr(i, 'name') for i in hentai.tags]
                end = time.time()
                await ctx.send(f'Cover: {cover} \n'
                               f'**English Title:** {english_title if english_title else "none"} \n'
                               f'**Japanese Title:** {japanese_title if japanese_title else "none"} \n'
                               f'**Pages:** {pages} \n'
                               f'**Link:** {link} \n'
                               f'**Tags:** {", ".join(tags)}')
                await ctx.send(f'(Time Elapsed: {round(end - start, 4)} seconds)')
            except ValueError:
                await ctx.send("Sorry, I'm unable to decode the sauce that you sent.")

    @commands.command()
    async def random(self, ctx, items=None):
        try:
            if items is None:
                await ctx.send("Here's how to use this: \n"
                               f'```{config["PREFIX"]}random <number of sauces>```')
            elif 1 <= int(items) <= 25:
                prompt = "Gathering nuke codes..."
                await ctx.send(prompt if int(items) <= 20 else prompt + " (this might take a while)")
                start = time.time()
                results = [nhentai.get_random_id() for i in range(int(items))]
                end = time.time()
                await ctx.send(f'Here ya go: `{results}`\n\n'
                               f'(Time Elapsed: {round(end - start, 2)} seconds)')
            else:
                await ctx.send("Sorry, can't send you **that** many nuke codes.")
        except ValueError:
            await ctx.send("Only enter **numbers** for an amount, you dipshit.")


def setup(client):
    client.add_cog(NHentai(client))
