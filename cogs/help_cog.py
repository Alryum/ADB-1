from discord.ext import commands


class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Музыка:
!help - отображает все доступные команды
!p !play !играть <keywords> - находит видео на ютубе по ключевым словам или по прямой ссылке и начинает его проигрывать
!queue !q !очередь - отображает текущую очередь
!skip !s !скип - пропускает текущий трек
!clear !с - очищает очередь
!leave !d - отключить бота от голосового канала
!pause !пауза - пауза/продолжить
!resume !r - продолжить

Другое:
!cat - случайное изображение кота в чат
!dog - случайное изображение собаки в чат
!ping - проверить бота на предмет жизни
```
"""

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
