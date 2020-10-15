import discord
import random

from discord.ext import commands
from index import config


def mock_func(sentence) -> str:
    new_sentence = ""
    capital = 0
    small = 0
    for letter in sentence.lower():
        randomizer = random.randint(0, 1)
        if capital == 2 or small == 2:
            new_sentence += letter.upper() if small == 2 else letter.lower()
            capital, small = 0, 0
        else:
            if randomizer == 1:
                capital += 1
                new_sentence += letter.upper()
            else:
                small += 1
                new_sentence += letter.lower()

    return new_sentence


class Mockery(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mock(self, ctx, user: discord.User = None):
        try:
            if user is None:
                await ctx.send(f'`{config["PREFIX"]}mock <@mentioned_user>` to *mockify* their last message.')
            else:
                counter = 0  # pseudo-counter
                # iterates through the latest 100 messages
                async for message in ctx.channel.history():
                    # if any of those message's author matches the mentioned user
                    if message.author.id == user.id:
                        # checks if the author is the send itself
                        # and if we skipped one time already
                        if message.author.id == ctx.author.id and counter < 1:
                            counter += 1
                            pass    # skips to the next last message
                        else:
                            new_message = mock_func(message.content)
                            await ctx.send(f"***{new_message}***")
                            break
        except ValueError:
            await ctx.send("There seems to be an error with your input, please try again.")

    @commands.command()
    async def mockify(self, ctx, *, sentence=None):
        if sentence is None:
            await ctx.send(f'`{config["PREFIX"]}mockify <sentence>` to mockify it.')
        else:
            new_message = mock_func(sentence)
            await ctx.send(f"***{new_message}***")


def setup(client):
    client.add_cog(Mockery(client))
