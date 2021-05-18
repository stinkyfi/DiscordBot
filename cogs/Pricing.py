# Imports
from pip._vendor import requests
import requests
import discord
from discord.ext import commands, tasks
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

    @tasks.loop(seconds=30)
    async def gas_check(self):
        print('gas_check>>>')
        api = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=' + config.etherscan['api_key']
        response = requests.get(api)
        # Setting `Streaming ` status
        try:
            gwei = response.json()['result']['ProposeGasPrice'] + ' Gwei'
        except ValueError:
            gwei = "Offline"
        print(gwei)
        await main.client.change_presence(activity=discord.Streaming(name=gwei, url='https://etherscan.io/gastracker'))
        print('<<<gas_check')
        return gwei

    @commands.command()
    async def gascheck(self, ctx):
        print('gascheck>>>')
        api = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=' + config.etherscan['api_key']
        response = requests.get(api)
        link = "https://etherscan.io/gastracker"
        header = "Fat Lenny's ETH Gas/Deli Station"
        embed = discord.Embed(title=header, url=link, description="Prices provided by Etherscan", color=0xdb0000)
        embed.set_thumbnail(url="https://i.ibb.co/sCsYDqm/fat-pepes-deli.png")
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
        embed.set_footer(text="Now buy something or get out")
        print("average: " + str(average))
        print("price: " + str(price))
        long = price / pow(10, 9)
        gwei = long
        print("1 gwei: " + str(gwei))
        total = float(gwei) * average
        print("total ETH: " + str(total))
        dollar = total * price
        dollar = dollar * gwei
        print("total USD: " + str(dollar))
        print('<<<gascheck')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Pricing(client))
