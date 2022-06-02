from time import time
import discord
from discord.ext import commands
from discord.utils import get
import json
import asyncio
from datetime import datetime, date, time, timezone


#好色喔 偷看ㄌㄌ

bot=commands.Bot(command_prefix='!')

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata= json.load(jfile)

voice_channel_id=980462768979333245
##text_channel_id=981490326990643291
role_id=981622801926615180
h_role_id=981845025178652693
##user_id=536882521141411851
h_channel_portal_id=981855600461881434


@bot.event
async def on_ready(): #啟動
    print("ㄌㄌ起床了")
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="GHOST / 星街すいせい"))





@bot.event
async def on_voice_state_update(member,before, after): #進入指定語音聊天室時自動給予身分組 離開時移除
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
                
        
@bot.command()  #建立指定身分私人聊天區
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


@bot.event
async def on_message(message): #機器人回復訊息
    if bot.user.mentioned_in(message):
        await message.channel.send("₍ᐢ •͈ ༝ •͈ ᐢ₎？")
        if message.content.endswith('我好愛你'):
            await asyncio.sleep(2)
            await message.channel.send('變態')
        else:
            await message.channel.send('窩不知道(,,•́.•̀,,)')

    if message.content.startswith('你會做什麼'):
        await asyncio.sleep(1)
        await message.channel.send('我會睡覺 zz')

    if message.content.startswith('我好愛你'):
        await asyncio.sleep(1)
        await message.channel.send('變態')

    if message.content.startswith('星爆'):
        pic = discord.File(jdata['pic'])
        await message.channel.send(file=pic) #file name= C:\\Users\\louie\\Documents\\GitHub\\TEST\\picture\\UfXTSPn.gif

    



    if message.content.startswith('星街'): #星街廚
        await message.channel.send('☄️✨☄️✨☄️')
        await message.channel.send('https://twitter.com/suisei_hosimati')
        await message.channel.send('https://www.youtube.com/channel/UC5CwaMl1eIgY8h02uZw7u8A')

    
        

               
##for i in member.roles:
    ##if str(i) =='休息':
        ##print(i)
                    
        ##break


if __name__ =="__main__":
    bot.run(jdata['Token'])
