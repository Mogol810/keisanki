import discord
import datetime
import os
from time import sleep
from discord.ext import tasks


client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
@client.event
async def on_ready():
    print('ログインしました')
    time_check.start()

async def Sendyosyu():
    channel=client.get_channel(729329464575787088)
    await channel.send('皆さん計算機概論の復習課題はお済ですか？今日までの課題です。')

async def Sendhukusyu():
    channel=client.get_channel(729329464575787088)
    await channel.send('皆さん計算機概論の予習課題はお済ですか？明日の授業時間までの課題です。')

@tasks.loop(seconds=60)
async def time_check():
    date = datetime.date.today()
    timedate = datetime.datetime.now()
    now = timedate.strftime('%H:%M')
    if date.weekday() == 3:
        if now == '07:00':
            await Sendyosyu()
            
    if date.weekday() == 6:
        if now == '07:00':
            await Sendhukusyu()
                
                

client.run(token)
