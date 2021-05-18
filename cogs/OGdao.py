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
import config
import main


class OGdao(commands.Cog):

    def __init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ogdao cog loaded")

    @commands.command()
    @commands.has_role('discord-og')
    async def gnosis(self, ctx):
        print('gnosis>>>')
        # Get ETH balance
        api = 'https://api.etherscan.io/api?module=account&action=balance&address' \
              '=0x2d51cB37805c559B376232B0a9879fA7914d27E0&tag=latest&apikey=' + config.etherscan['api_key']
        response = requests.get(api)
        eth_balance = response.json()['result']
        total_eth = Decimal(float(eth_balance) / 1000000000000000000)

        # Get ETH/USD
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
        eth_usd = requests.get(api).json()['ethereum']['usd']
        # Get ETH/EURO
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur'
        eth_eur = requests.get(api).json()['ethereum']['eur']
        # Get ETH/AUD
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=aud'
        eth_aud = requests.get(api).json()['ethereum']['aud']

        # Format currencies
        usd_price = "(${:0,.2f})".format(total_eth * Decimal(eth_usd))
        eur_price = "(€{:0,.2f})".format(total_eth * Decimal(eth_eur))
        aud_price = "(${:0,.2f})".format(total_eth * Decimal(eth_aud))

        # Embedded Message
        header = "<:OGDAO:839642965546106900> OGDAO Gnosis Safe"
        link = 'https://gnosis-safe.io/app/#/safes/0x2d51cB37805c559B376232B0a9879fA7914d27E0/balances'
        embed = discord.Embed(title=header, url=link, color=Color.green())
        embed.set_thumbnail(url="https://docs.gnosis.io/safe/img/gnosis_safe_logo_green.png")
        embed.add_field(name="ETH", value="{:.4f} ETH ".format(total_eth), inline=False)
        embed.add_field(name="USD", value=usd_price)
        embed.add_field(name="EURO", value=eur_price)
        embed.add_field(name="AUD", value=aud_price)
        embed.set_footer(text="Prices from Coingecko.com")
        print('<<<gnosis')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('discord-og')
    async def vote(self, ctx):
        print('vote>>>')
        # Declarations
        proposals, voter = [], []
        poll = {}
        # API call to get snapshot proposals
        response = requests.get('https://hub.snapshot.page/api/ebog.eth/proposals')
        # Pull Proposal Hashes
        for prop in response.json():
            # Add proposal hashes into an array, so we can iterate
            proposals.append(prop)
        # Using each hash, pull individual proposal data
        for prop_data in proposals:
            # Proposal data
            end = response.json()[prop_data]['msg']['payload']['end']
            # start = response.json()[prop_data]['msg']['payload']['start']
            body = response.json()[prop_data]['msg']['payload']['body']
            body = (body[:2040] + '..') if len(body) > 2042 else body
            # If the proposal end time is greater than now, it is an active proposal
            if end > time.time():
                link = "https://snapshot.org/#/ebog.eth/proposal/" + prop_data
                header = '<:OGDAO:839642965546106900> ' + response.json()[prop_data]['msg']['payload']['name']
                embed = discord.Embed(title=header, url=link, description=body,
                                      color=Color.magenta())
                embed.set_thumbnail(
                    url='https://gblobscdn.gitbook.com/spaces%2F-MG4Ulnnabb2Xz3Lei9_%2Favatar-1602311890000.png')

                # embed.add_field(name="Starts:",
                #               value=str(datetime.fromtimestamp(start)))
                embed.add_field(name="Expires:",
                                value=str(datetime.fromtimestamp(end)), inline=False)
                # Get specific proposal data
                api = 'https://hub.snapshot.page/api/ebog.eth/proposal/' + prop_data
                props = requests.get(api).json()
                total = 0

                # Pull Proposal Hashes
                for votes in props:
                    voter.append(votes)

                for voter_data in voter:
                    if props[voter_data]['msg']['payload']['choice'] in poll:
                        poll[props[voter_data]['msg']['payload']['choice']] += 1
                        total += 1
                    else:
                        poll[props[voter_data]['msg']['payload']['choice']] = 1
                        total += 1
                for key in poll:
                    # 1, 0 are default for proposals. Converts 1,0 into Yes, No
                    # If the key is not 1,0, then display the key value
                    if key == 1:
                        option = 'Yes'
                    elif key == 0:
                        option = 'No'
                    else:
                        option = key
                    embed.add_field(name=option,
                                    value=str(poll[key]) + '/155')
                # If there is only one answer, add a No with 0 votes
                if len(poll) == 1:
                    embed.add_field(name='No',
                                    value='0/155')
                embed.add_field(name="Link:",
                                value='https://snapshot.org/#/ebog.eth/proposal/' + prop_data, inline=False)
                embed.set_footer(text="Follow Us on twitter: @EBOGDAO")
                print('<<<gnosis')
                await ctx.send(embed=embed)

    @commands.command()
    async def twitter(self, ctx):
        print('twitter>>>')
        link = "https://twitter.com/EBOGDAO"
        header = "Twitter: @EBOGDAO"
        embed = discord.Embed(title=header, url=link, color=Color.blue())
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1389787778129358849/zkgm31D6_400x400.jpg")
        embed.add_field(name="Link:", value='https://twitter.com/EBOGDAO')
        embed.set_footer(text="Follow Us on twitter: @EBOGDAO")
        print('<<<gnosis')
        await ctx.send(embed=embed)

    @commands.command()
    async def lp26(self, ctx):
        print('lp26>>>')
        link = "https://eulerbeats.com/enigma/1280018153728"
        header = "Enigma LP 26"
        embed = discord.Embed(title=header, url=link, color=Color.dark_purple())
        embed.set_thumbnail(url="https://i.ibb.co/7SDbC4X/LP26.gif")
        embed.add_field(name="Link:", value=link)
        print('<<<gnosis')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('manager')
    async def announce_proposal(self, ctx, arg):
        print('announce_proposal>>>')
        proposals, voter = [], []
        poll = {}
        response = requests.get('https://hub.snapshot.page/api/ebog.eth/proposals')
        prop_data = str(arg)
        end = response.json()[prop_data]['msg']['payload']['end']
        body = response.json()[prop_data]['msg']['payload']['body']
        body = (body[:2040] + '..') if len(body) > 2040 else body
        # If the proposal end time is greater than now, it is an active proposal
        if end > time.time():
            link = "https://snapshot.org/#/ebog.eth/proposal/" + str(arg)
            header = '<:OGDAO:839642965546106900> ' + response.json()[prop_data]['msg']['payload']['name']
            embed = discord.Embed(title=header, url=link, description=body,
                                  color=Color.magenta())
            embed.set_thumbnail(
                url='https://gblobscdn.gitbook.com/spaces%2F-MG4Ulnnabb2Xz3Lei9_%2Favatar-1602311890000.png')
            embed.add_field(name="Expires:",
                            value=str(datetime.fromtimestamp(end)), inline=False)
            api = 'https://hub.snapshot.page/api/ebog.eth/proposal/' + prop_data
            print(api)
            props = requests.get(api).json()
            total = 0
            # Pull Proposal Hashes
            for votes in props:
                voter.append(votes)

            for voter_data in voter:

                if props[voter_data]['msg']['payload']['choice'] in poll:
                    poll[props[voter_data]['msg']['payload']['choice']] += 1
                    total += 1
                else:
                    poll[props[voter_data]['msg']['payload']['choice']] = 1
                    total += 1
            for key in poll:
                if key == 1:
                    option = 'Yes'
                elif key == 0:
                    option = 'No'
                else:
                    option = key
                embed.add_field(name=option,
                                value=str(poll[key]) + '/88')
            if len(poll) == 1:
                embed.add_field(name='No',
                                value='0/88')
            embed.add_field(name="Link:",
                            value='https://snapshot.org/#/ebog.eth/proposal/' + prop_data, inline=False)
            embed.set_footer(text="Follow Us on twitter: @EBOGDAO")
            channel = main.client.get_channel(config.discord['channel_announcements'])
            print('<<<announce_proposal')
            await channel.send(embed=embed)


def setup(client):
    client.add_cog(OGdao(client))
