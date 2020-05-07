from discord.ext import commands
import logging

logger = logging.getLogger('bot')

DEV_IDS = [173123135321800704, 166337116106653696] # Sven, border

def is_dev():
    async def predicate(ctx):
        return ctx.author.id in DEV_IDS
    return commands.check(predicate)

class Comp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.utility = bot.get_cog("Utility")

    #===Commands===#        

    # addtime [type] [time] [optional link]
    # removetime [type] [time] (only owner or admin/staff)
    # addcomp/addchallenge [type] [explanation for comp info] (only admin/staff)
    # removecomp/removechallenge [type] (only admin/staff)
    # comp/challenge/competition [opt. type] [opt. number]
        # if type left blank
            # COF 2 - 1st BorderKeeper (4m31s) [link if posted], 2nd Sven (4m30s) 3rd Tim (15m21s)
            # KoTH - ...
        # if type specified
            # King of The Hill
            # 1st - BorderKeeper (4m31s) [Link if posted] 
            # 2nd - Sven (4m30s)
            # 3rd - Tim  (15m21s)[Link if posted]
            # ... will post more if number specified
    # comptypes/challengetypes
        # will give a list of competitions available and short info about them

    @commands.command()
    async def addtime(self, ctx, *args):
        """Add a time into the running of a specific competition
        Usage:
            .addtime type time video_link
            --Get type name from .comptypes. Specify time as 2:54 as in 2m and 54s. Link is optional.
        """
        arguments = " ".join(args)
        attachments = ctx.message.attachments
        filename = attachments[0].filename

        logger.debug(".addtime called")

        await self.utility.send_message(channel, message)

        return

    @commands.command()
    @is_dev()
    async def runscript(self, ctx, *args):
        """Runs an sql script in a local database

        Usage:
            .runscript SELECT * FROM table WHERE x = 2
        """

        #TODO: Move to admin.py cog, will leave it here until it is finished

        query = " ".join(args)
        await self.utility.send_message(channel, message)

        return

    #===Utility===#

    async def send_message(self, channel, message: str):
        """Send a message to the text channel"""

        await channel.trigger_typing()
        newMessage = await channel.send(message)

        logger.info("Sent message to {} : {}".format(channel, newMessage.content))

        return newMessage

def setup(bot):
    bot.add_cog(Comp(bot))