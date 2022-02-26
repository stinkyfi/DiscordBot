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


class TwistedTech(commands.Cog):

    def __init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("TwistdTech cog loaded")

    @commands.command()
    @commands.has_role('Twisted Team')
    async def safe(self, ctx):
        print('gnosis>>>')
        # Get FTM balance
        api = 'https://api.ftmscan.com/api?module=account&action=balance&address=' \
              '0xe2A1c9df8313b02a6476f78d2e8Bfcff28f373bf&tag=latest&apikey=' + tt_config.ftmscan['api_key']
        response = requests.get(api)
        eth_balance = response.json()['result']
        total_eth = Decimal(float(eth_balance) / 1000000000000000000)

        # Get FTM/USD
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=fantom&vs_currencies=usd'
        ftm_usd = requests.get(api).json()['fantom']['usd']
        # Get FTM/EURO
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=fantom&vs_currencies=eur'
        ftm_eur = requests.get(api).json()['fantom']['eur']
        # Get FTM/AUD
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=fantom&vs_currencies=aud'
        ftm_aud = requests.get(api).json()['fantom']['aud']

        # Format currencies
        usd_price = "(${:0,.2f})".format(total_eth * Decimal(ftm_usd))
        eur_price = "(€{:0,.2f})".format(total_eth * Decimal(ftm_eur))
        aud_price = "(${:0,.2f})".format(total_eth * Decimal(ftm_aud))

        # Embedded Message
        header = "Twisted Tech Gnosis Safe"
        link = 'https://gnosis-safe.io/app/#/safes/0x2d51cB37805c559B376232B0a9879fA7914d27E0/balances'
        embed = discord.Embed(title=header, url=link, color=Color.green())
        embed.set_thumbnail(url="https://i.ibb.co/YBz3M35/logo-square-simple-400px.jpg")
        embed.add_field(name="FTM", value="{:.4f} FTM ".format(total_eth), inline=False)
        embed.add_field(name="USD", value=usd_price)
        embed.add_field(name="EURO", value=eur_price)
        embed.add_field(name="AUD", value=aud_price)
        embed.set_footer(text="Prices from Coingecko.com")
        print('<<<gnosis')
        await ctx.send(embed=embed)

    @commands.command()
    async def twitter(self, ctx):
        print('twitter>>>')
        link = "https://twitter.com/twistedtechnfts"
        header = "Twitter: @twistedtechnfts"
        embed = discord.Embed(title=header, url=link, color=Color.blue())
        embed.set_thumbnail(
            url="https://cdn.cms-twdigitalassets.com/content/dam/about-twitter/en/brand-toolkit/brand-download-img-1"
                ".jpg.twimg.2560.jpg")
        embed.add_field(name="Link:", value='https://twitter.com/twistedtechnfts')
        embed.set_footer(text="Follow Us on twitter: @twistedtechnfts")
        print('<<<gnosis')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Twisted Team')
    async def announcement(self, ctx):
        print('announce_proposal>>>')
        header = '$NOFS POAP Snapshot'
        link = 'https://github.com/TwistedTech-wtf/NightmareOnFantomSt/blob/main/snapshots/NOFS-POAP.txt'
        body = "@everyone If you minted a $NOFS (Nightmare on Fantom St.) NFT, you will be receiving a free POAP. " \
               "Please review " \
               "the text file for your address, if you do not see your address and feel like there is a mistake. " \
               "Please use the #❓-technical-support channel.  Use the search function to verify your address is on " \
               "the list.  "
        embed = discord.Embed(title=header, url=link, description=body,
                              color=Color.magenta())
        embed.add_field(name="Link:",
                        value=link, inline=False)
        embed.set_footer(text="Follow Us on twitter: @TwistedTechNFTs")
        channel = main.client.get_channel(894780403322351626)
        await channel.send(embed=embed)

    @commands.command()
    async def poap(self, ctx):
        print('poap>>>')
        header = '$NOFS POAP Claim'
        link = 'https://poap.delivery/nofs'
        body = "Thank you for supporting TwistedTech and being an OG. Please claim this POAP as proof of your early " \
               "support. Only available to $NOFS minters"
        embed = discord.Embed(title=header, url=link, description=body,
                              color=Color.dark_orange())
        embed.set_thumbnail(url="https://i.ibb.co/Mp7s83P/MOFS-POAP1.png")
        embed.add_field(name="Link:",
                        value=link, inline=False)
        embed.set_footer(text="Follow Us on twitter: @TwistedTechNFTs")
        print('<<<poap')
        await ctx.send(embed=embed)

    @commands.command()
    async def tune_vault(self, ctx):
        print('gnosis>>>')
        # Get FTM balance
        api = 'https://api.ftmscan.com/api?module=account&action=balance&address=' \
              '0x6ea2983B15F7272689B0fdb15275219dEF2d5F1A&tag=latest&apikey=' + tt_config.ftmscan['api_key']
        response = requests.get(api)
        eth_balance = response.json()['result']
        total_eth = Decimal(float(eth_balance) / 1000000000000000000)
        total_eth = total_eth / 10

        # Get FTM/USD
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=fantom&vs_currencies=usd'
        ftm_usd = requests.get(api).json()['fantom']['usd']
        # Get FTM/EURO
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=fantom&vs_currencies=eur'
        ftm_eur = requests.get(api).json()['fantom']['eur']
        # Get FTM/AUD
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=fantom&vs_currencies=aud'
        ftm_aud = requests.get(api).json()['fantom']['aud']

        # Format currencies
        usd_price = "(${:0,.2f})".format(total_eth * Decimal(ftm_usd))
        eur_price = "(€{:0,.2f})".format(total_eth * Decimal(ftm_eur))
        aud_price = "(${:0,.2f})".format(total_eth * Decimal(ftm_aud))

        # Embedded Message
        header = "TUNE Songwriting Prize"
        link = ''
        embed = discord.Embed(title=header, url=link, color=Color.blue())
        embed.set_thumbnail(url="https://i2.wp.com/genxsingapore.com/wp-content/uploads/2021/10/moneybank.gif")
        embed.add_field(name="Rules", value="The more you mint, the more the pot grows", inline=False)
        embed.add_field(name="FTM", value="{:.4f} FTM ".format(total_eth), inline=False)
        embed.add_field(name="USD", value=usd_price)
        embed.add_field(name="EURO", value=eur_price)
        embed.add_field(name="AUD", value=aud_price)
        embed.set_footer(text="Prices from Coingecko.com")
        print('<<<gnosis')
        await ctx.send(embed=embed)

    @commands.command()
    async def plaguepits(self, ctx):
        print('PlaguePits>>>')

        # Embedded Message
        header = "The $BLOOD Bank Proposes a PlaguePits Test"
        link = ''
        embed = discord.Embed(title=header, url=link, color=Color.dark_red())
        embed.set_thumbnail(url="https://i.ibb.co/0QMHV4S/Plague-Pits-POAP1.png")
        embed.add_field(name="FTMSCAN", value="This test will be conducted on FTMScan to show how the Plague Pits "
                                              "work before launch of webapp.", inline=False)
        embed.add_field(name="Participate", value="This is an opportunity to raise your score before the webapp launch")
        embed.add_field(name="Rewards", value="A special POAP will be awarded to all participatns of the test. As "
                                              "well as $BLOOD prizes")
        embed.set_footer(text="Estimated test December 26th")
        print('<<<PlaguePits')
        await ctx.send(embed=embed)

    @commands.command()
    async def presale(self, ctx):
        print('Presale>>>')

        # Embedded Message
        header = "$BLOOD Presale.Money"
        link = 'https://presale.money/app/#/presale/40'
        embed = discord.Embed(title=header, url=link, color=Color.dark_purple())
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1397648992008392714/_qQf1S8N_400x400.png")
        embed.add_field(name="Buy Cheap", value="Buy $BLOOD at a lower rate than initial listing on Spookyswap",
                        inline=False)
        embed.add_field(name="LP is locked", value="75% of funds raised go directly into a locked LP. Securing the "
                                                   "Market")
        embed.set_footer(text="Sale from December 22 - January 1st")
        print('<<<Presale')
        await ctx.send(embed=embed)

    @commands.command()
    async def bubo(self, ctx):
        api = "https://api.ftmscan.com/api?module=stats&action=tokensupply&contractaddress" \
                 "=0x9b1372e4a65d914d670f061913ad746250533b49&apikey=1ZXM4HW5X9TAN4GGRCJ27JJN2D1WYWFZWF "
        response = requests.get(api)
        supply = response.json()['result']
        header = "$BUBO Analytics"
        embed = discord.Embed(title=header, url='', color=Color.dark_red())
        embed.set_thumbnail(url="https://i.ibb.co/tX7TSXk/BUBONIC-BASTARDS.png")
        embed.add_field(name="Address", value="0x9b1372e4a65d914d670f061913ad746250533b49", inline=False)
        embed.add_field(name="Possible Players", value=supply, inline=False)
        embed.add_field(name="$BLOOD Emission Start:", value="Friday, December 24, 2021 3:00:00 PM GTM")
        embed.add_field(name="$BLOOD Emission End:", value="Thursday, March 24, 2022 3:00:00 PM GTM")
        embed.add_field(name="$BLOOD Per Day:", value="166.666666667", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def blood(self, ctx):
        api = "https://api.ftmscan.com/api?module=stats&action=tokensupply&contractaddress" \
                 "=0xa75bdbC03a9E5ea6E695Aa3E8321f181F61d0fae&apikey=1ZXM4HW5X9TAN4GGRCJ27JJN2D1WYWFZWF "
        response = requests.get(api)
        supply = response.json()['result']
        supply = Decimal(float(supply) / 1000000000000000000)
        header = "$BUBO Analytics"
        embed = discord.Embed(title=header, url='', color=Color.gold())
        embed.set_thumbnail(url="https://i.ibb.co/g6kj0GF/BLOOD-official.png")
        embed.add_field(name="Address", value="0xa75bdbC03a9E5ea6E695Aa3E8321f181F61d0fae", inline=False)
        embed.add_field(name="Total Supply:", value="{:,}".format(supply))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(TwistedTech(client))
