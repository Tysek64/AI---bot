import discord
from discord.ext import commands
from AI import AI
import os

bot = commands.Bot(intents = discord.Intents.all(), command_prefix='Hello, ')

@bot.event
async def on_ready():
  print("Hello, world!")

@bot.listen('on_message')
async def reply (ctx):
  await ctx.send(AI(Message.content))

token = os.environ("TOKEN")
bot.run(token)