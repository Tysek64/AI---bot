import discord
from discord.ext import commands
from AI import AI
from AI import emojify
import os

bot = commands.Bot(intents = discord.Intents.all(), command_prefix='A')

@bot.event
async def on_ready():
  print("Hello, world!")

@bot.command(name='I,')
async def sendReply (ctx, *, question="ﷺ"):
  if question != "ﷺ":
    await ctx.send(AI(question))
  else:
    await ctx.send("I couldn't hear you. Could you repeat?")

@bot.command(name='I,tell,')
async def sendReply (ctx, *, question="ﷺ"):
  if question != "ﷺ":
    await ctx.send("/tts "+AI(question))
  else:
    await ctx.send("/tts I couldn't hear you. Could you repeat?")

@bot.command(name='I,emojify,')
async def sendReply (ctx, *, question="ﷺ"):
  if question != "ﷺ":
    await ctx.send(emojify(question))
  else:
    await ctx.send("I couldn't hear you. Could you repeat?")

token = os.environ.get("TOKEN")
bot.run(token)