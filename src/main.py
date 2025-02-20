import discord
from discord.ext import commands
import google.generativeai as genai
import logging
from _cmd import all_cmds
from slash_cmds import all_slash_cmds

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

logging.basicConfig(format='(%(asctime)s) - %(levelname)s: %(message)s: %(process)d',
                    datefmt='%Y-%m-%d %H:%M:%S (%z)', level=logging.INFO, filename='bot-logs/vector.log', filemode='w')

logger = logging.getLogger(__name__)


@bot.event
async def on_ready():
    await bot.tree.sync()
    activity = discord.Game(name='!q <query>')
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f"We have logged in as {bot.user}")


@bot.command(name='q')
async def hello(ctx):

    genai.configure(api_key="API-KEY")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    try:
        user = ctx.author
        user_input = ctx.message.content
        response = model.generate_content(user_input)
        logger.info(
            f'User requested a query: {ctx.message.content}, successfully generated response')

        embed = discord.Embed(
            title=f"{user_input}",
            description=response.text,
            color=discord.Color.blue()
        )
        embed.set_footer(text=f"Requested by {user.name}",
                         icon_url=user.avatar.url if user.avatar else user.default_avatar.url)

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
    finally:
        logger.info('command executed')


all_cmds(bot)
all_slash_cmds(bot)

# bot token
bot.run("BOT-TOKEN")
