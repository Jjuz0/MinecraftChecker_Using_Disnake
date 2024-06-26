
import asyncio
import disnake
from disnake.ext import commands, tasks
from disnake import Option
from disnake import TextInputStyle 
from config import token # type: ignore
import requests
from datetime import datetime


async def get_server_status():
    response = requests.get('https://api.mcstatus.io/v2/status/java/worst-practice.ru')
    response_json = response.json()

    embed = disnake.Embed(title="Состояние сервера", color=0x00ff00)
    current_time = datetime.now()
    timestamp = int(datetime.timestamp(current_time))

    if response_json['online']:
        online_status = f'<t:{timestamp}:R>'
        player_count = response_json['players']['online']
        player_max = response_json['players']['max']
        embed.add_field(name="Cервер работает в штатном режиме!", value=online_status, inline=False)
        embed.add_field(name="Игроки онлайн:                             Версия сервера:", value=f'{player_count}/{player_max}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀1.16.5 → 1.21', inline=False)
        #embed.add_field(name="Версия сервера:", value=f'1.16.5 → 1.21', inline=False)
    else:
        online_status = f'<t:{timestamp}:R>'
        embed.add_field(name="Сервер Выключен!", value=online_status, inline=False)
        return embed
    
    embed.set_thumbnail(url="https://api.mcstatus.io/v2/icon/worst-practice.ru")
    return embed

intents = disnake.Intents.default()
intents.message_content = True


client = disnake.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=disnake.Intents.all())


bot.load_extension("cogs.minecraftchecker")
@bot.event
async def on_ready():
    print(f'Бот готов! Подключен к {bot.user.name}')
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="Проблемы создателя", status = disnake.Status.online))
    edit_message.start()


@tasks.loop(seconds=30)  # Измени интервал, если необходимо
async def edit_message():
    channel = bot.get_channel(1242546892345315380)  # Замени на ID канала
    message = await channel.fetch_message(1255450328908959775)  # Замени на ID сообщения
    new_embed = await get_server_status()
    await message.edit(embed=new_embed)

@edit_message.before_loop
async def before_edit_message():
    await bot.wait_until_ready()


bot.run(token)




















  







