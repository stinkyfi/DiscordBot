#########################################
#
# Project: Fat Lenny Discord Bot
# Original Author: StinkyFi
# Opened OG DAO: 6/9/2021
# Contributors: swaHili
# Version: 1.0.3
#########################################

# Imports
import os
from discord.ext import commands
# Custom Config
import config

illegal_words = []
# Enter a prefix you would like to use to interact with your bot
client = commands.Bot(command_prefix='$lenny ')
bot_key = config.discord[0]['bot_key']


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(str(bot_key))
