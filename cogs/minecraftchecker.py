import disnake
from disnake.ext import commands
import asyncio
from disnake import TextInputStyle
from disnake.ext import commands, tasks
from disnake import Option
import urllib.parse
import random
import requests
import pprint

response = requests.get('https://api.mcstatus.io/v2/status/java/funtime.su') #замени funtime.su на нужные тебе IP
response_json = response.json()
#pprint.pprint(response_json)
#print(response.text)
print(response_json['players'])
class MinecraftChecker(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx, text: str = None):
        if text == None:
            await ctx.send("Введите Айпи сервера!")
            return 
        response = requests.get(f'https://api.mcstatus.io/v2/status/java/{text}')
        response_json = response.json()

        if response_json['online']:
            online_status = 'Сервер онлайн'
        else:
            online_status = 'Сервер оффлайн'

        player_count = response_json['players']['online']

        await ctx.send(f'{online_status}\nКоличество игроков онлайн: {player_count}')









def setup(bot:commands.Bot):
    bot.add_cog(MinecraftChecker(bot))
    print(f"{__name__} загружен.")