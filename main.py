# -*- coding: utf-8 -*-
import asyncio
import discord
import os
entry_id = 736628061289578496
server_id = 736622331178254426
hello_id = 737068025253200069

server_id = int(server_id)
entry_id = int(entry_id)
hello_id = int(hello_id)
client = discord.Client()
print("CotTyan Mark II V 2.5.0")
print("Copyright (c) 2020 T, Laminne Yamamoto")
async def send(channel,*args, **kwargs): return await channel.send(*args, **kwargs)

@client.event
async def on_member_join(member):
    lrn = []
    for role in member.roles:
        lrn.append(role.name)
        if len(lrn) == 2:
            break
    m = "Hi!<@"+str(member.id)+">,\nPlease read <#736628061289578496> and type [ok]. \nIf you are going to to be able to do it, please introduse yourself in <#736627134604378143>.\n"
    channel = client.get_channel(737576896476348447)
    await channel.send(m)
    
@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.guild.id == server_id:
        if message.content == "ok":
            lrn = []
            for role in message.author.roles:
                lrn.append(role.name)
                if len(lrn) == 2:
                    return
            role = discord.utils.get(message.guild.roles, name="自己紹介してね")
            return await message.author.add_roles(role)
            message_to = "<@"+str(member.id)+">,\nPlease introduse yourself in <#736627134604378143>.\n"
            channel = client.get_channel(737576896476348447)
            return await channel.send(message_to)

client.run(os.environ['MARK1_TOKEN'])
