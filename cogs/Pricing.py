# Imports
from pip._vendor import requests
import requests
import discord
from discord.ext import commands, tasks
from discord import Color
from decimal import Decimal
import time
import math
# Custom Config
import config
import main


class Pricing(commands.Cog):

    def __init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.gas_check.start()
        print("Pricing cog loaded")

    def cog_unload(self):
        self.gas_check.cancel()

    @tasks.loop(seconds=120)
    async def gas_check(self):
        print('gas_check>>>')
        # api = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=' + config.etherscan['api_key']
        # response = requests.get(api)
        api = 'https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=' \
              '0x9091C144218D3Ab99C716833404B74A87aea4c74&apikey=' + config.etherscan['api_key']
        response = requests.get(api)
        # Setting `Streaming ` status
        try:
            # gwei = response.json()['result']['ProposeGasPrice'] + ' Dwarfs'
            gwei = response.json()['result'] + ' Dwarfs'
        except ValueError:
            gwei = "Offline"
        print(gwei)
        await main.client.change_presence(activity=discord.Streaming(name=gwei, url='https://etherscan.io'))
        print('<<<gas_check')
        return gwei

    @commands.command()
    async def gascheck(self, ctx):
        print('gascheck>>>')
        api = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=' + config.etherscan['api_key']
        response = requests.get(api)
        link = "https://etherscan.io/gastracker"
        header = "Dwarf Putins, Ethereum Gas Station"
        embed = discord.Embed(title=header, url=link, description="Prices provided by Etherscan", color=0xdb0000)
        embed.set_thumbnail(url="https://i.ibb.co/1mJdmZq/Putin-Dwarf-Gas-Logo.png")
        embed.add_field(name=":fuelpump:Regular", value=response.json()['result']['SafeGasPrice'] + ' Gwei')
        embed.add_field(name=":fuelpump:Plus", value=response.json()['result']['ProposeGasPrice'] + ' Gwei')
        embed.add_field(name=":fuelpump:Supreme", value=response.json()['result']['FastGasPrice'] + ' Gwei')
        average = float(response.json()['result']['ProposeGasPrice'])
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
        response = requests.get(api)
        # Setting `Streaming ` status
        try:
            price = float(response.json()['ethereum']['usd'])
        except ValueError:
            price = "Offline"
        embed.set_footer(text="Dwarf Putin controls the gas pipeline from Etherescan to Discord")
        print("average: " + str(average))
        print("price: " + str(Decimal(price)))
        eth_gwei = Decimal(0.000000001 * average)
        gas_usd = eth_gwei * Decimal(price)
        print(eth_gwei)
        print(gas_usd)
        long = price / pow(10, 9)
        gwei = long
        print("1 gwei: " + str(gwei))
        print("Math: " + str(float(gwei)) + ' * ' + str(average))
        total = float(gwei) ** average
        print("total ETH: " + str(total))
        dollar = total * price
        dollar = dollar * gwei
        print("total USD: " + str(dollar))
        print('<<<gascheck')
        await ctx.send(embed=embed)


    @commands.command()
    async def ethbalance(self, ctx, arg):
        api = 'https://api.etherscan.io/api?module=account&action=balance&address=' + str(arg) + '&tag=latest&apikey='\
              + config.etherscan['api_key']
        response = requests.get(api)
        eth_balance = response.json()['result']
        total_eth = Decimal(float(eth_balance) / 1000000000000000000)
        total = "<a:knucklesroll:802355992850726973> Fat Knuckles ETH Balance Sheets\n" + "```{:.4f}ETH ".format(total_eth)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
        response = requests.get(api)
        # Setting `Streaming ` status
        print(response.json()['ethereum']['usd'])
        price = total_eth * Decimal(response.json()['ethereum']['usd'])
        price = "(${:0,.2f})".format(price)
        total += str(price) + "```"
        await ctx.channel.send(total)

    @commands.command()
    async def sushibar(self, ctx):
        epoch = time.time()
        epoch = math.trunc(epoch)
        apy, apr = "", ""
        api = 'https://api2.sushipro.io/?action=get_xsushi_apy&from=1632494793&to=' + str(epoch)
        response = requests.get(api)
        datas = response.json()[1]
        for data in datas:
            apy = str("{:0,.2f}".format(data['apy'])) + '%'
            apr = str("{:0,.2f}".format(data['apr'])) + '%'
            break
        header = "Gas Station xSUSHI Bar"
        desc = "Current Rewards are: "
        embed = discord.Embed(title=header, url="", description=desc, color=Color.gold())
        embed.set_thumbnail(url="https://app.sushi.com/_next/image?url=%2Fxsushi-sign.png&w=1920&q=75")
        embed.add_field(name="APY", value=apy)
        embed.add_field(name="APR", value=apr)
        embed.set_footer(text="Powered by: SushiSwap API")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Pricing(client))
