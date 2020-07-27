import discord
import datetime 
import os
from time import sleep

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    while True:
        date = datetime.date.today()
        timedate = datetime.datetime.now()
        now = timedate.strftime('%H:%M')
        if date.weekday() == 2:
            if now == '22:00':
                channel = client.get_channel(737221401584336916)
                await channel.send('皆さん計算機概論の復習課題はお済ですか？今日までの課題です。')
                sleep(60)
        if date.weekday() == 5:
            if now == '22:00':
                channel = client.get_channel(737221401584336916)
                await channel.send('皆さん計算機概論の予習課題はお済ですか？明日の授業開始時間までの課題です。')
                sleep(60)
                
                

client.run(TOKEN)
