from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")  # type: ignore

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def showstats(ctx, arg):
    await ctx.send(arg)


bot.run(token=TOKEN)
