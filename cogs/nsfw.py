import nhentai
import discord

from discord.ext import commands
from index import config


class NHentai(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def decode(self, ctx, sauce=None):
        if sauce is None:
            await ctx.send('Please enter the sauce first: \n\n'
                           f'```{config["PREFIX"]}decode <sauce>```')
        else:
            try:
                hentai = nhentai.get_doujin(int(sauce))
                cover = hentai.cover
                english_title = hentai.titles.get("english")
                japanese_title = hentai.titles.get("japanese")
                pages = str(len(hentai.pages))
                link = "||https://nhentai.net/g/" + sauce + "||"
                tags = [getattr(i, 'name') for i in hentai.tags]
                await ctx.send(f'Cover: {cover} \n'
                               f'English Title: {english_title if english_title else "none"} \n'
                               f'Japanese Title: {japanese_title if japanese_title else "none"} \n'
                               f'Link: {link} \n'
                               f'Tags: {", ".join(tags)}')
            except ValueError:
                await ctx.send("Sorry, I'm unable to decode the sauce that you sent.")


def setup(client):
    client.add_cog(NHentai(client))
