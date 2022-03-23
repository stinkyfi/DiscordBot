# Imports
import operator
from pip._vendor import requests
import discord
from discord.ext import commands


class CultofCrypto(commands.Cog):

    def __init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("cultOfCrypto cog loaded")

    @commands.command()
    async def fantasy_stinky(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=yearn-finance&vs_currencies=usd'
        res = requests.get(api)
        yfi = res.json()['yearn-finance']['usd']
        total += float(yfi) * 0.048069
        yfi = "${:0,.2f}".format(yfi * 0.048069)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=reserve-rights-token&vs_currencies=usd'
        res = requests.get(api)
        rsr = res.json()['reserve-rights-token']['usd']
        total += float(rsr) * 20000
        rsr = "${:0,.2f}".format(rsr * 20000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=inverse-finance&vs_currencies=usd'
        res = requests.get(api)
        inv = res.json()['inverse-finance']['usd']
        total += float(inv) * 5
        inv = "${:0,.2f}".format(inv * 5)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=sushi&vs_currencies=usd'
        res = requests.get(api)
        sushi = res.json()['sushi']['usd']
        total += float(sushi) * 50
        sushi = "${:0,.2f}".format(sushi * 50)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=thorchain&vs_currencies=usd'
        res = requests.get(api)
        rune = res.json()['thorchain']['usd']
        total += float(rune) * 20
        rune = "${:0,.2f}".format(rune * 20)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=wmatic&vs_currencies=usd'
        res = requests.get(api)
        matic = res.json()['wmatic']['usd']
        total += float(matic) * 1000
        matic = "${:0,.2f}".format(matic * 1000)
        header = "Stinky Fantasy Score"
        embed = discord.Embed(title=header, description="Prices provided by Coingecko",
                              color=discord.Color.dark_green())
        embed.set_thumbnail(url="https://media1.giphy.com/media/NVBR6cLvUjV9C/giphy.gif")
        embed.add_field(name="YFI (0.048069): ", value=yfi, inline=False)
        embed.add_field(name="RSR (2000): ", value=rsr, inline=False)
        embed.add_field(name="INV (5): ", value=inv, inline=False)
        embed.add_field(name="SUSHI (50): ", value=sushi, inline=False)
        embed.add_field(name="RUNE (20): ", value=rune, inline=False)
        embed.add_field(name="MATIC (1000): ", value=matic, inline=False)
        total = "${:0,.2f}".format(total) + ' (' + "{:0,.2f}".format(total - 10000) + ')'
        embed.add_field(name="Total: ", value=str(total), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fantasy_auto(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=enjincoin&vs_currencies=usd'
        res = requests.get(api)
        enj = res.json()['enjincoin']['usd']
        total += float(enj) * 2500
        enj = "${:0,.2f}".format(enj * 2500)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ankr&vs_currencies=usd'
        res = requests.get(api)
        ankr = res.json()['ankr']['usd']
        total += float(ankr) * 5500
        ankr = "${:0,.2f}".format(ankr * 5500)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=wmatic&vs_currencies=usd'
        res = requests.get(api)
        matic = res.json()['wmatic']['usd']
        total += float(matic) * 6500
        matic = "${:0,.2f}".format(matic * 6500)
        header = "Auto Fantasy Score"
        embed = discord.Embed(title=header, description="Prices provided by Coingecko", color=discord.Color.gold())
        embed.set_thumbnail(url="https://f3louisville.files.wordpress.com/2019/07/giphy-3.gif")
        embed.add_field(name="ENJ (2500): ", value=enj, inline=False)
        embed.add_field(name="MATIC (6500): ", value=matic, inline=False)
        embed.add_field(name="ANKR (5500): ", value=ankr, inline=False)
        total = "${:0,.2f}".format(total) + ' (' + "{:0,.2f}".format(total - 10000) + ')'
        embed.add_field(name="Total: ", value=str(total), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fantasy_drdoom(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=curve-dao-token&vs_currencies=usd'
        res = requests.get(api)
        crv = res.json()['curve-dao-token']['usd']
        total += float(crv) * 1000
        crv = "${:0,.2f}".format(crv * 1000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=aave&vs_currencies=usd'
        res = requests.get(api)
        aave = res.json()['aave']['usd']
        total += float(aave) * 4.5
        aave = "${:0,.2f}".format(aave * 4.5)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=havven&vs_currencies=usd'
        res = requests.get(api)
        snx = res.json()['havven']['usd']
        total += float(snx) * 100
        snx = "${:0,.2f}".format(snx * 100)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=thorchain&vs_currencies=usd'
        res = requests.get(api)
        rune = res.json()['thorchain']['usd']
        total += float(rune) * 100
        rune = "${:0,.2f}".format(rune * 100)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=inverse-finance&vs_currencies=usd'
        res = requests.get(api)
        inv = res.json()['inverse-finance']['usd']
        total += float(inv) * 5
        inv = "${:0,.2f}".format(inv * 5)
        header = "Dr. Doom Fantasy Score"
        embed = discord.Embed(title=header, description="Prices provided by Coingecko",
                              color=discord.Color.dark_purple())
        embed.set_thumbnail(
            url="http://static.comicvine.com/uploads/original/11111/111119363/3874525-9224525733-36604.gif")
        embed.add_field(name="CRV (1000): ", value=crv, inline=False)
        embed.add_field(name="RUNE (100): ", value=rune, inline=False)
        embed.add_field(name="AAVE (4.5): ", value=aave, inline=False)
        embed.add_field(name="SNX (100): ", value=snx, inline=False)
        embed.add_field(name="INV (5): ", value=inv, inline=False)
        total = "${:0,.2f}".format(total) + ' (' + "{:0,.2f}".format(total - 10000) + ')'
        embed.add_field(name="Total: ", value=str(total), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fantasy_erik(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd'
        res = requests.get(api)
        xrp = res.json()['ripple']['usd']
        total += float(xrp) * 6900
        xrp = "${:0,.2f}".format(xrp * 6900)
        header = "Erik's Fantasy Score"
        embed = discord.Embed(title=header, description="Prices provided by Coingecko", color=discord.Color.dark_red())
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/765427862260940800/838306347069603861/1611101728440_1.gif")
        embed.add_field(name="XRP (6900): ", value=xrp, inline=False)
        total = "${:0,.2f}".format(total) + ' (' + "{:0,.2f}".format(total - 10000) + ')'
        embed.add_field(name="Total: ", value=str(total), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fantasy_apevan(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=reserve-rights-token&vs_currencies=usd'
        res = requests.get(api)
        rsr = res.json()['reserve-rights-token']['usd']
        total += float(rsr) * 31907
        rsr = "${:0,.2f}".format(rsr * 31907)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ankr&vs_currencies=usd'
        res = requests.get(api)
        ankr = res.json()['ankr']['usd']
        total += float(ankr) * 11923
        ankr = "${:0,.2f}".format(ankr * 11923)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=vechain&vs_currencies=usd'
        res = requests.get(api)
        vet = res.json()['vechain']['usd']
        total += float(vet) * 11477
        vet = "${:0,.2f}".format(vet * 11477)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=bittorrent&vs_currencies=usd'
        res = requests.get(api)
        btt = res.json()['bittorrent']['usd']
        total += float(btt) * 11923
        btt = "${:0,.2f}".format(btt * 11923)
        header = "Ape-van's Fantasy Score"
        embed = discord.Embed(title=header, description="Prices provided by Coingecko", color=discord.Color.blue())
        embed.set_thumbnail(url="https://media4.giphy.com/media/TUMBjT9u5LmV2/200.gif")
        embed.add_field(name="BTT (11923): ", value=btt, inline=False)
        embed.add_field(name="RSR (31907): ", value=rsr, inline=False)
        embed.add_field(name="ANKR (11923): ", value=ankr, inline=False)
        embed.add_field(name="VET (11477): ", value=vet, inline=False)
        total = "${:0,.2f}".format(total) + ' (' + "{:0,.2f}".format(total - 10000) + ')'
        embed.add_field(name="Total: ", value=str(total), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fantasy_zoiby(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd&vs_currencies=usd'
        res = requests.get(api)
        shib = "{:f}".format(float(res.json()['shiba-inu']['usd']))
        print(shib)
        print(float(shib) * 534760000)
        total += float(shib) * 534760000
        shib = "${:0,.2f}".format(float(shib) * 534760000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=the-graph&vs_currencies=usd'
        res = requests.get(api)
        grt = res.json()['the-graph']['usd']
        total += float(grt) * 1000
        grt = "${:0,.2f}".format(grt * 1000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=wmatic&vs_currencies=usd'
        res = requests.get(api)
        matic = res.json()['wmatic']['usd']
        total += float(matic) * 5000
        matic = "${:0,.2f}".format(matic * 5000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=usd'
        res = requests.get(api)
        theta = res.json()['theta-token']['usd']
        total += float(theta) * 100
        theta = "${:0,.2f}".format(theta * 100)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=algorand&vs_currencies=usd'
        res = requests.get(api)
        algo = res.json()['algorand']['usd']
        total += float(algo) * 1000
        algo = "${:0,.2f}".format(algo * 1000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd'
        res = requests.get(api)
        sol = res.json()['solana']['usd']
        total += float(sol) * 90
        sol = "${:0,.2f}".format(sol * 90)
        header = "Zoiby's Fantasy Score"
        embed = discord.Embed(title=header, description="Prices provided by Coingecko", color=discord.Color.red())
        embed.set_thumbnail(url="https://media.tenor.com/images/b2ed564c134fafbd56351538ba51f2f0/tenor.gif")
        embed.add_field(name="SHIB (534760000): ", value=shib, inline=False)
        embed.add_field(name="GRT (1000): ", value=grt, inline=False)
        embed.add_field(name="MATIC (5000): ", value=matic, inline=False)
        embed.add_field(name="THETA (100): ", value=theta, inline=False)
        embed.add_field(name="ALGO (1000): ", value=algo, inline=False)
        embed.add_field(name="SOL (90): ", value=sol, inline=False)
        total = "${:0,.2f}".format(total) + ' (' + "{:0,.2f}".format(total - 10000) + ')'
        embed.add_field(name="Total: ", value=str(total), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fantasy_hellbent(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=inverse-finance&vs_currencies=usd'
        res = requests.get(api)
        inv = res.json()['inverse-finance']['usd']
        total += float(inv) * 5
        inv = "${:0,.2f}".format(inv * 5)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=akropolis&vs_currencies=usd'
        res = requests.get(api)
        akro = res.json()['akropolis']['usd']
        total += float(akro) * 10000
        akro = "${:0,.2f}".format(akro * 10000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=unit-protocol-duck&vs_currencies=usd'
        res = requests.get(api)
        duck = res.json()['unit-protocol-duck']['usd']
        total += float(duck) * 1500
        duck = "${:0,.2f}".format(duck * 1500)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=badger-dao&vs_currencies=usd'
        res = requests.get(api)
        badger = res.json()['badger-dao']['usd']
        total += float(badger) * 40
        badger = "${:0,.2f}".format(badger * 40)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=reserve-rights-token&vs_currencies=usd'
        res = requests.get(api)
        rsr = res.json()['reserve-rights-token']['usd']
        total += float(rsr) * 5000
        rsr = "${:0,.2f}".format(rsr * 5000)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=sushi&vs_currencies=usd'
        res = requests.get(api)
        sushi = res.json()['sushi']['usd']
        total += float(sushi) * 126
        sushi = "${:0,.2f}".format(sushi * 126)
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=republic-protocol&vs_currencies=usd'
        res = requests.get(api)
        ren = res.json()['republic-protocol']['usd']
        total += float(ren) * 1000
        ren = "${:0,.2f}".format(ren * 1000)
        header = "Hellbent's Fantasy Score"
        embed = discord.Embed(title=header, description="Prices provided by Coingecko", color=discord.Color.orange())
        embed.set_thumbnail(url="https://i.pinimg.com/originals/09/b6/3c/09b63c0732639ae7526d793b7addcbfb.gif")
        embed.add_field(name="INV (5): ", value=inv, inline=False)
        embed.add_field(name="AKRO (10000): ", value=akro, inline=False)
        embed.add_field(name="DUCK (1500): ", value=duck, inline=False)
        embed.add_field(name="BADGER (40): ", value=badger, inline=False)
        embed.add_field(name="RSR (5000): ", value=rsr, inline=False)
        embed.add_field(name="SUSHI (126): ", value=sushi, inline=False)
        embed.add_field(name="REN (1000): ", value=ren, inline=False)
        total = "${:0,.2f}".format(total) + ' (' + "{:0,.2f}".format(total - 10000) + ')'
        embed.add_field(name="Total: ", value=str(total), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fantasy_leaderboard(self, ctx):
        players = {}
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=inverse-finance&vs_currencies=usd'
        res = requests.get(api)
        inv = res.json()['inverse-finance']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=akropolis&vs_currencies=usd'
        res = requests.get(api)
        akro = res.json()['akropolis']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=yearn-finance&vs_currencies=usd'
        res = requests.get(api)
        yfi = res.json()['yearn-finance']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=curve-dao-token&vs_currencies=usd'
        res = requests.get(api)
        crv = res.json()['curve-dao-token']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=thorchain&vs_currencies=usd'
        res = requests.get(api)
        rune = res.json()['thorchain']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=aave&vs_currencies=usd'
        res = requests.get(api)
        aave = res.json()['aave']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=havven&vs_currencies=usd'
        res = requests.get(api)
        snx = res.json()['havven']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=bittorrent&vs_currencies=usd'
        res = requests.get(api)
        btt = res.json()['bittorrent']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=reserve-rights-token&vs_currencies=usd'
        res = requests.get(api)
        rsr = res.json()['reserve-rights-token']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ankr&vs_currencies=usd'
        res = requests.get(api)
        ankr = res.json()['ankr']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=vechain&vs_currencies=usd'
        res = requests.get(api)
        vet = res.json()['vechain']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=unit-protocol-duck&vs_currencies=usd'
        res = requests.get(api)
        duck = res.json()['unit-protocol-duck']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=badger-dao&vs_currencies=usd'
        res = requests.get(api)
        badger = res.json()['badger-dao']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=sushi&vs_currencies=usd'
        res = requests.get(api)
        sushi = res.json()['sushi']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=republic-protocol&vs_currencies=usd'
        res = requests.get(api)
        ren = res.json()['republic-protocol']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd'
        res = requests.get(api)
        xrp = res.json()['ripple']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd&vs_currencies=usd'
        res = requests.get(api)
        shib = "{:f}".format(float(res.json()['shiba-inu']['usd']))
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=the-graph&vs_currencies=usd'
        res = requests.get(api)
        grt = res.json()['the-graph']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=wmatic&vs_currencies=usd'
        res = requests.get(api)
        matic = res.json()['wmatic']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=usd'
        res = requests.get(api)
        theta = res.json()['theta-token']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=algorand&vs_currencies=usd'
        res = requests.get(api)
        algo = res.json()['algorand']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd'
        res = requests.get(api)
        sol = res.json()['solana']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=yearn-finance&vs_currencies=usd'
        res = requests.get(api)
        yfi = res.json()['yearn-finance']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=thorchain&vs_currencies=usd'
        res = requests.get(api)
        rune = res.json()['thorchain']['usd']
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=enjincoin&vs_currencies=usd'
        res = requests.get(api)
        enj = res.json()['enjincoin']['usd']

        players['Erik'] = float("{:.2f}".format(float(xrp) * 6900))
        players['Auto'] = float("{:.2f}".format((float(enj) * 2500) + (float(matic) * 6500) + (float(ankr) * 5500)))
        players['Stinky'] = float("{:.2f}".format((float(yfi) * 0.048069) + (float(rsr) * 20000) + (float(inv) * 5) +
                                                  (float(sushi) * 50) + (float(rune) * 20) + (float(matic) * 1000)))
        players['Dr. Doom'] = float("{:.2f}".format((float(crv) * 1000) + (float(aave) * 4.5) + (float(snx) * 100) +
                                                    (float(rune) * 100) + (float(inv) * 5)))
        players['ApeVan'] = float("{:.2f}".format((float(rsr) * 31907) + (float(ankr) * 11923) +
                                                  (float(vet) * 11477) + (float(btt) * 11923)))
        players['Zoiby'] = float(
            "{:.2f}".format((float(shib) * 534760000) + (float(grt) * 1000) + (float(matic) * 5000) +
                            (float(theta) * 100) + (float(algo) * 1000) + (float(sol) * 90)))
        players['Hellbent'] = float("{:.2f}".format((float(inv) * 5) + (float(akro) * 10000) + (float(duck) * 1500) +
                                                    (float(badger) * 40) + (float(rsr) * 5000) + (float(sushi) * 126) +
                                                    (float(ren) * 1000)))
        header = 'Fantasy Crypto Championship'
        link = 'https://cdn.discordapp.com/attachments/830926417977409567/840435727186919434/Leaderboard.gif'
        embed = discord.Embed(title=header, url='', description="Live Leaderboard", color=0xdb0000)
        embed.set_thumbnail(url=link)
        i = 1
        board = dict(sorted(players.items(), key=operator.itemgetter(1), reverse=True))
        for key in list(board.keys()):
            print(key + " " + str(players[key]))
            if players[key] > 10000:
                diff = players[key] - 10000
                user = str(i) + '.) ' + str(key) + ' (+$' + str("{:,.2f}".format(diff)) + ')'
            else:
                diff = 10000 - players[key]
                user = str(i) + '.) ' + str(key) + ' (-$' + str("{:,.2f}".format(diff)) + ')'
            i += 1
            embed.add_field(name=user,
                            value='$' + str("{:,.2f}".format(players[key])), inline=False)
        embed.set_footer(text="Prices Powered by Coingecko")
        await ctx.send(embed=embed)


    @commands.command()
    async def NFTL(self, ctx):
        total = 0
        api = 'https://api.coingecko.com/api/v3/simple/price?ids=nifty-league&vs_currencies=usd'
        res = requests.get(api)
        nftl = "$" + str(res.json()['nifty-league']['usd'])
        header = "$NFTL (Nifty League)"
        embed = discord.Embed(title=header, description="", color=discord.Color.dark_blue())
        embed.set_thumbnail(
            url="https://nifty-league.com/static/media/nl_logo.e6d4a3c5.png")
        embed.add_field(name="USD Value", value=nftl, inline=False)
        embed.set_footer(text="Prices from Coingecko.com")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CultofCrypto(client))
