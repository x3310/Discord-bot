from pickle import NONE
from time import time
import discord
from discord.ext import commands, tasks
from discord.utils import get
import json
import asyncio
import requests
import re
import tweepy
from tweepy import Stream
#from tweepy.streaming import StreamListener

from datetime import datetime, date, time, timezone


#好色喔 偷看ㄌㄌ

bot=commands.Bot(command_prefix='!') #機器人啟動指令

#調用.json
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata= json.load(jfile)

voice_channel_id=980462768979333245
##text_channel_id=981490326990643291
role_id=981622801926615180
bot_id=981483671527784469
h_role_id=981845025178652693
h_channel_portal_id=981855600461881434
##user_id=536882521141411851



@bot.event
async def on_ready(): #啟動
    print("ㄌㄌ起床了")
    await asyncio.sleep(5)
    
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="GHOST / 星街すいせい"))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="🎊１５０万人見守り配信🎊【ホロライブ / 星街すいせい 】"))




@bot.event #進入指定語音聊天室時自動給予身分組 離開時移除
async def on_voice_state_update(member,before, after): 
    if before.channel is None and after.channel is not None:
        if str(after.channel.id) == str(voice_channel_id):

            print(f'{member.name} join {after.channel.name}!')
            timestamp = datetime.now() #進入語音時間                        
            print(timestamp.strftime(r"in 20%y/%m/%d %p %I:%M:%S"))
            print(" ")
           
            guild=bot.get_guild(member.guild.id)
            role=guild.get_role(role_id)
            await member.add_roles(role)
    elif before.channel is not None and after.channel is None:
        
        print(f'{member.name} leave {before.channel.name}!')
        timestamp = datetime.now() #離開語音時間                   
        print(timestamp.strftime(r"in 20%y/%m/%d %p %I:%M:%S"))
        print(" ")

        guild=bot.get_guild(member.guild.id)
        role=guild.get_role(role_id)
       
        await member.remove_roles(role)
                
        
@bot.command() #建立指定身分私人聊天區
async def open_chat(ctx):
        guild = ctx.guild
        print(guild)
        member = get(guild.roles, name="聊天")
        print(member)
        admin_role = ctx.guild
        print(admin_role)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True),
            admin_role: discord.PermissionOverwrite(read_messages=False)
        }
        guild = ctx.message.guild
        await guild.create_text_channel('聊天',overwrites=overwrites)


#貼圖ID:981848358903771186

@bot.event #在特定訊息加入反應後新增身分組
async def on_raw_reaction_add(data):
    if data.message_id == h_channel_portal_id: 
        if str(data.emoji) == '<:h_123:981848358903771186>':
            guild=bot.get_guild(data.guild_id)
            print(f'{data.member}進入:D!')
            role=guild.get_role(h_role_id)
            await data.member.add_roles(role)
         

@bot.event #在特定訊息移除反應後刪除身分組
async def on_raw_reaction_remove(data):
    if data.message_id == h_channel_portal_id:
        if str(data.emoji) == '<:h_123:981848358903771186>':
            guild=bot.get_guild(data.guild_id)
            user = await guild.fetch_member(data.user_id)
            print(f'{user}離開:D!')
            role=guild.get_role(h_role_id)
            await user.remove_roles(role)

@bot.command() #播放指定音樂
async def welcome(context):
    
    user=context.message.author
    channel = user.guild.get_channel(voice_channel_id)

    if bot.voice_clients != []:
        vc=context.voice_client
        await context.message.delete()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=jdata['閃光']))
    else:
        vc=await channel.connect()
        await context.message.delete()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=jdata['閃光']))


@bot.command() #播放指定音樂
async def ghost(context):
    
    user=context.message.author
    print(f'{user}播放Ghost!')
    print(" ")
    channel = user.guild.get_channel(voice_channel_id)

    if bot.voice_clients != []:
        vc=context.voice_client
        await context.message.delete()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=jdata['Ghost']))
    else:
        vc=await channel.connect()
        await context.message.delete()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=jdata['Ghost']))


@bot.command() #播放 恩
async def hentai(context):
    
    user=context.message.author
    print(f'{user}覺得變態!')
    print(" ")
    channel = user.guild.get_channel(voice_channel_id)

    if bot.voice_clients != []:
        vc=context.voice_client
        await context.message.delete()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=jdata['hentai']))
    else:
        vc=await channel.connect()
        await context.message.delete()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=jdata['hentai']))
        

@bot.command() #機器人離開聊天室
async def leave(context):
    await context.voice_client.disconnect()
    




@bot.event #機器人回復訊息
async def on_message(message): 
    #機器人被提及
    if bot.user.mentioned_in(message): 
        await message.channel.send("₍ᐢ •͈ ༝ •͈ ᐢ₎？")
        if message.content.endswith('我好愛你'):
            await asyncio.sleep(2)
            await message.channel.send('變態')

        elif message.content.startswith('hi'):
            await message.channel.send('安安')

        elif message.content.endswith('你會做什麼'):
            await message.channel.send('我會睡覺 zz')
        
        elif message.content.endswith('你在做什麼'):
            await message.channel.send('我在聽歌')
            await message.channel.send('https://www.youtube.com/watch?v=IKKar5SS29E')


        elif message.content.endswith('你畫我猜ㄇ?'):
             await message.channel.send('好啊')

        else:
            await message.channel.send('窩不知道(,,•́.•̀,,)')
            
    #機器人收到關鍵字
    if message.content.startswith('星爆'):
        picture = discord.File(jdata['星爆'])
        await message.channel.send(file=picture) #file name in setting.json
    
    if message.content.startswith('確實'):
        picture = discord.File(jdata['確實'])
        await message.channel.send(file=picture)

    if message.content.startswith('騙人'):
        picture = discord.File(jdata['騙人的吧'])
        await message.channel.send(file=picture)
    
    if message.content.endswith('sus'):
        picture = discord.File(jdata['Rock_Sus'])
        await message.channel.send(file=picture)

    #機器人是星街廚
    if message.content.startswith('星街'): 
        await message.channel.send('☄️✨☄️✨☄️')
        await message.channel.send('https://twitter.com/suisei_hosimati')
        await message.channel.send('https://www.youtube.com/channel/UC5CwaMl1eIgY8h02uZw7u8A')

    await bot.process_commands(message)


#每300秒檢查一次
#@tasks.loop(seconds=300)
#指令型
@bot.command()
async def suisei(context):
    with open("youtubedata.json",mode='r',encoding='utf8') as yfile:
        data=json.load(yfile)
 
  
    print("檢查中!")

  #檢查在Youtubedata.json的所有頻道
    for youtube_channel in data:
        print(f"現在檢查{data[youtube_channel]['channel_name']}...")
    #獲取頻道網址
        channel = f"https://www.youtube.com/channel/{youtube_channel}"
    #獲取頻道/videos頁面
        html = requests.get(channel+"/videos").text
    #獲取最新影片網址
        try:
            latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
        except: #如果頻道無任何影片則跳過
            continue

    #比對最新影片與存檔影片的不同
    if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:

        #修改Youtubedata.json的最新影片資料
        data[str(youtube_channel)]['latest_video_url'] = latest_video_url
        with open("youtubedata.json", "w") as yfile:
            json.dump(data, yfile)

        #獲取指令發送頻道
        discord_channel_id = context.channel.id
        discord_channel = bot.get_channel(int(discord_channel_id))
        #傳送訊息
        await discord_channel.send (f"{data[str(youtube_channel)]['channel_name']} 正在直播: {latest_video_url}")
     
    elif str(data[youtube_channel]["latest_video_url"]) == latest_video_url:
        #獲取指令發送頻道
        discord_channel_id = context.channel.id
        discord_channel = bot.get_channel(int(discord_channel_id))
        #傳送訊息
        await discord_channel.send (f"{data[str(youtube_channel)]['channel_name']} 現在沒有在直播")
 
               
##for i in member.roles:
    ##if str(i) =='休息':
        ##print(i)
                    
        ##break


if __name__ =="__main__":
    bot.run(jdata['Token'])
