import discord
import datetime 
from time import sleep


TOKEN = "NzM3MjEwMjAyMDAwMTk1NjU1.Xx6CgA.UtdHTdIzQoJf06OKNfWm3J8_eH4"  
client = discord.Client()

@client.event
async def on_ready():
    while True:
        date = datetime.date.today()
        timedate = datetime.datetime.now()
        now = timedate.strftime('%H:%M')
        if date.weekday() == 3:
            if now == '07:00':
                channel = client.get_channel(737221401584336916)
                await channel.send('皆さん計算機概論の復習課題はお済ですか？今日までの課題です。')
                sleep(60)
        if date.weekday() == 6:
            if now == '07:00':
                channel = client.get_channel(737221401584336916)
                await channel.send('皆さん計算機概論の予習課題はお済ですか？明日の授業開始時間までの課題です。')
                sleep(60)
                
                

client.run('TOKEN_OF_YOUR_BOT')
