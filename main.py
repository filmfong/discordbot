import discord, time, os, asyncio, random
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(
      self_bot = True,
      command_prefix = "!"
)

@bot.event
async def on_ready():
    print('-' * 20)
    print('Loged in as') 
    print(f'User: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('-' * 20)

@bot.command()
async def ping(ctx):
      ping = round(bot.latency * 1000)
      await ctx.send(f"Pong! {ping}ms")


@bot.event
async def on_reaction_add(reaction, user):
    # channel = bot.get_channel(1206886702413774859)
    # if not channel:
    #     return
        if reaction.message.author.bot == True:
            if reaction.emoji.name == "Swrd4":
                time.sleep(3)
                await reaction.message.add_reaction(reaction)
                print (f" [@] | {reaction.message.channel.name} | Joined Rumble Royale Event at {time.strftime('%X')}")
                
            
            
TOKEN = "TOKEN" #or use env 
bot.run(TOKEN, bot = False)
