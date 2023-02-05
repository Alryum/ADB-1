import discord
import logging
import tomli
from discord.ext import commands

import os
import img_operations.animal_pic as animal_pic
import img_operations.image_distortion as image_distortion
from cogs.music_cog import music_cog
from cogs.help_cog import help_cog

handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')

with open('config.toml', mode='rb') as cf:
    config = tomli.load(cf)

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))
    print(f'Logged in as {bot.user}')


@bot.command()
async def ping(ctx):
    await ctx.send('На месте спортсмены')


@bot.command()
async def cat(ctx):
    await ctx.send(animal_pic.get_random_cat_link())


@bot.command()
async def dog(ctx):
    await ctx.send(animal_pic.get_random_dog_link())


@bot.command()
async def defish(ctx):
    img_name = image_distortion.defish(
        ctx.message.attachments[0].url, ctx.message.author.id)
    await ctx.send(file=discord.File(img_name))
    await os.remove(img_name)

bot.remove_command('help')
bot.run(config['TOKEN'], log_handler=handler)
