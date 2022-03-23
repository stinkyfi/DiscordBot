# Imports
from decimal import Decimal
import time
from datetime import datetime
from pip._vendor import requests
import requests
import discord
from discord import Color
from discord.ext import commands
from discord.ext.commands import Context
# Custom Config
import tt_config
import main
import re
import os
import mmap

class DegenDwarfs(commands.Cog):

    def __init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("TwistdTech cog loaded")


    @commands.command()
    @commands.has_role('TECHNICALSUPPORT')
    async def shortlist(self, client, message: discord.Message):
        print(message.content)
        print(message.author.id)
        id = str(message.author.id)
        addr = str(message.content)
        channel = client.get_channel(801689630880694294)
        # match the regex statements for the input of the ID and the
        if re.match(r"^(0x)[0-9a-fA-F]{40}$", addr) and re.match(r"^[0-9]{18}$", id):
            file = "data.txt"

            # if the file has contents

            if os.path.getsize(file) > 0:
                with open(file, "r") as f:
                    for line in f.readlines():
                        if id in line and addr in line:
                            return "Found your address your on the white list"
                        elif id in line:
                            message = "Please contact a Team member to update your address"
                            await channel.send(message)
                        elif addr in line:
                            message = "This address is already reported by another user"
                            await channel.send(message)
                f.close()


            # check for previous occourances
            # if it finds it, it does not write it back into the file
            if os.path.getsize(file) > 0:
                with open(file, "r+") as f:
                    for index, line in enumerate(f.readlines()):
                        if id not in line or addr not in line:
                            break
                        else:

                            f.write(line)
                f.close()

            # write data
            with open(file, 'a+') as f:
                f.write(id + ", " + addr + "\n")
            f.close()

            message = "@{} address accepted `{}`".format(id, addr[0:5] + "..." + addr[-4:])
        else:
            message = "@{} address format incorrect, it should be 0x`40 characters as a mix of 0-9 / a-f / A-F`".format(id)

        await channel.send(message)

    @commands.command()
    async def supply(self, ctx):
        api = 'https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress='\
                '0x9091C144218D3Ab99C716833404B74A87aea4c74&apikey=' + config.etherscan['api_key']
        response = requests.get(api)
        supply = response.json()['result']
        header = "Dwarf Analytics"
        link = 'https://etherscan.io/address/0x9091c144218d3ab99c716833404b74a87aea4c74?utm_source=icy.tools'
        embed = discord.Embed(title=header, url=link, color=Color.gold())
        embed.set_thumbnail(url="https://degendwarfs.io/static/media/degen-dwarfs.ceeb8582.png")
        embed.add_field(name="Address", value="0x9091C144218D3Ab99C716833404B74A87aea4c74", inline=False)
        embed.add_field(name="Dwarf Population", value=supply, inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_role('Team')
    async def contract(self, ctx):
        api = 'https://api.etherscan.io/api?module=account&action=balance&address='\
              '0x9091C144218D3Ab99C716833404B74A87aea4c74&tag=latest&apikey=' + config.etherscan['api_key']
        response = requests.get(api)
        supply = response.json()['result']
        supply = Decimal(float(supply) / 1000000000000000000)
        header = "Degen Dwarf Contract Funds"
        link = 'https://etherscan.io/address/0x9091c144218d3ab99c716833404b74a87aea4c74?utm_source=icy.tools'
        embed = discord.Embed(title=header, url=link, color=Color.blue())
        embed.set_thumbnail(url="https://degendwarfs.io/static/media/degen-dwarfs.ceeb8582.png")
        embed.add_field(name="Address", value="0x9091C144218D3Ab99C716833404B74A87aea4c74", inline=False)
        embed.add_field(name="Value", value="{:.4f} ETH".format(supply), inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(DegenDwarfs(client))
