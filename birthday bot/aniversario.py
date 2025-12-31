# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import os

TOKEN = os.getenv("9BOysIJSIf9s6vM2PHogn93QhScxu1dy")
CANAL_ID = 1379573924529967175   # ID do canal

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    canal = bot.get_channel(CANAL_ID)
    await canal.send( "🎉 Feliz aniversário minato Que Deus te abençoe e sua família. "
        "que você cresça e pare de jogar Blox Fruits porque esse jogo não dá futuro. "
        "E que você ganhe um Ryzen 9 9950X3D com uma RTX 5090 pra rodar 1k fps"
    )
    await bot.close()

bot.run(TOKEN)