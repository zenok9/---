import discord 
from discord.ext import commands

Bot = commands.Bot(command_prefix = "!")
Bot.remove.command("help")

@Bot.event
async def on_read():
  print("Bot is online.")
  
 @Bot.command(pass_content = true)
async def ping():
  await Bot.say("pong")
  
 Bot.run("NTA2NDE3OTk5ODkzMjMzNjY0.W9bkgw.EvC65A0DXSbfQsp4XtMPxZpVWtk")
