import discord
from discord.ext import commands
import datetime
import time

timedelta = datetime.timedelta(hours=24)
timedelta_weekly = datetime.timedelta(days=7)


def epoch_time():
    global epochtime
    target_time = datetime.datetime.now() + timedelta  # For demonstration, I'm setting it to a day  from now.
    target_time_weekly = datetime.datetime.now() + timedelta_weekly  # For demonstration, I'm setting it to a day  from now.
    epochtime = int(target_time.timestamp())
    # epochtime_weekly = int(target_time_weekly.timestamp())
    print("this is the day {}", epochtime)
    return epochtime


TOKEN = 'YOUR_DISCORD_TOKEN'
CHANNEL_ID = 1234456  # Replace with your channel's ID
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # bot.

    channel = bot.get_channel(CHANNEL_ID)

    print(f"sending message<t:{epoch_time()}:R>")

    # delete previous event message
    await channel.purge(limit=100)

    # await channel.se

    # send messages to the discord channel

    # have bot  Mention @Maplers role
    await channel.send(f"<@&figureoutbotrole>")




    # angry animated emoji
    appangry = ":apbangry:"

    await channel.send(f":smile: **BOSS/EVENT DAILY RESET** <t:{epochtime}:R>")

    await bot.close()


bot.run(TOKEN)
