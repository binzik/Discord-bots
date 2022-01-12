import discord
from discord.ext import commands

client = commands.Bot(command_prefix="lidl:")
client.remove_command("help")

@client.event
async def on_ready():
    print("|Start|")

@client.command()
async def help(ctx):
    await ctx.send("Jak nie umiesz to chuj")
    print("help")


client.run("OTMwOTEyNDMzMzY5OTMxODE3.Yd8xww.I4MlzsdEn-6Nm3_cOgdc4v1GBLE")