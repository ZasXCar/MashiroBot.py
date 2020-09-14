import discord
import default
import os
from discord.ext import commands


config = default.get("config.json")
client = commands.Bot(command_prefix=config["PREFIX"])


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'**{extension}** extension has now been loaded.')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'**{extension}** extension has now been unloaded')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'**{extension}** extension has now been reloaded')


for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(config["TOKEN"])
