import asyncio
import requests
from discord.ext import commands, tasks

class StatusRotator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = "https://discord.com/api/v8/users/@me/settings"
        self.change_status.start()

    def cog_unload(self):
        self.change_status.stop()

    @tasks.loop(seconds=3)
    async def change_status(self):
        statuses = getattr(self, "statuses", [])
        if statuses:
            for status in statuses:
                await self._change_status(status)
                await asyncio.sleep(15)  # Wait for 3 seconds

    async def _change_status(self, message):
        header = {
            "authorization": ""
        }

        json_data = {
            "status": "dnd",
            "custom_status": {
                "text": message
            }
        }
        requests.patch(self.url, headers=header, json=json_data)

    @commands.command()
    async def setrotator(self, ctx, *, statuses):
        # Split statuses by commas
        self.statuses = [status.strip() for status in statuses.split(',')]
        await ctx.send("`-` **ROTATING STATUS HAVE BEEN SET**")

    @commands.command()
    async def stoprotator(self, ctx):
        self.change_status.stop()
        await ctx.send("`-` **STATUS ROTATION STOPPED**")

def setup(bot):
    bot.add_cog(StatusRotator(bot))