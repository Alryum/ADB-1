from discord.ext import commands
import requests


class animal_img_cog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def get_random_cat_link(self):
        response = requests.get('https://aws.random.cat/meow')
        cat_json = response.json()
        return (cat_json['file'])

    def get_random_dog_link(self):
        response = requests.get('https://random.dog/woof.json')
        dog_json = response.json()
        return (dog_json['url'])

    @commands.command(name='cat')
    async def cat(self, ctx):
        await ctx.send(self.get_random_cat_link())

    @commands.command(name='dog')
    async def dog(self, ctx):
        await ctx.send(self.get_random_dog_link())
