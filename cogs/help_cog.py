from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Музыка:
!help - отображает все доступные команды
!p !play <keywords> - находит видео на ютубе по ключевым словам или по прямой ссылке и начинает его проигрывать
!q - отображает текущую очередь
!skip - пропускает текущий трек
!clear - очищает очередь
!leave - отключить бота от голосового канала
!pause - пауза/продолжить
!resume - продолжить

Другое:
!cat - случайное изображение кота в чат
!dog - случайное изображение собаки в чат
!defish - пупит прикрепленное изображение (рыбий глаз)
!ping - проверить бота на предмет жизни
```
"""

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
