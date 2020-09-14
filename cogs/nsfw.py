import nhentai
import discord
from discord.ext import commands


class NHentai(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def decode(self, ctx, sauce: int):
        try:
            hentai = nhentai.get_doujin(sauce)
            cover = hentai.cover
            english_title = hentai.titles.get("english")
            japanese_title = hentai.titles.get("japanese")
            pages = str(len(hentai.pages))
            link = "||https://nhentai.net/g/" + str(sauce) + "||"
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
