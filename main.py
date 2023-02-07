import discord
import logging
import tomli
from discord.ext import commands

import os
import img_operations.animal_pic as animal_pic
import img_operations.image_distortion as image_distortion
from cogs.music_cog import music_cog
from cogs.help_cog import help_cog
from cogs.animal_img_cog import animal_img_cog

handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')

with open('config.toml', mode='rb') as cf:
    config = tomli.load(cf)

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(animal_img_cog(bot))
    print(f'Logged in as {bot.user}')


@bot.command()
async def ping(ctx):
    await ctx.send('На месте спортсмены')


bot.remove_command('help')
bot.run(config['TOKEN'], log_handler=handler)
