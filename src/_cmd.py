import discord
from discord.ext import commands
import psutil
import requests
import logging

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='vector.log', filemode='w')

logger = logging.getLogger(__name__)


def all_cmds(bot):
    @bot.command(name='cpu-usage')
    async def check_cpu_usage(ctx):
        try:

            logger.info('Checked CPU usage')
            user = ctx.author
            cpu_usage = psutil.cpu_percent()
            # await ctx.send(f"CPU usage: {cpu_usage}%")
            embed = discord.Embed(
                title='Your current CPU USAGE',
                description=f"{cpu_usage}%",
                color=discord.Color.yellow()
            )
            embed.set_footer(text=f"Requested by {user.name}",
                             icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
            await ctx.send(embed=embed)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
        finally:
            logger.info('command executed')

    @bot.command(name='memory-usage')
    async def memory_usage(ctx):
        try:
            logger.info('Checked memory usage')
            user = ctx.author
            mem_usage = psutil.Process()
            check = mem_usage.memory_info()
            embed = discord.Embed(
                title='Your current MEMORY USAGE',
                description=f'RSS: {check.rss} bytes\n VMS: {check.vms} bytes',
                color=discord.Color.blue()
            )
            embed.set_footer(text=f'Requested by {user.name}',
                             icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
            await ctx.send(embed=embed)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
        finally:
            logger.info('command executed')

    @bot.command(name='disk')
    async def disk(ctx):
        try:

            logger.info('Checked disk usage')
            logger.info('Checking disk usage...')
            user = ctx.author
            disk_use = psutil.disk_usage('/')
            embed = discord.Embed(
                description=f'**TOTAL DISK SPACE AVAILABLE**: {disk_use.total}\n **TOTAL SPACE AVAILABLE**: {disk_use.free}\n **TOTAL SPACE IN USE**: {disk_use.used}\n **HERE IS THE TOTAL % OF DISK YOUR DISK USE**: {disk_use.percent}',
                color=discord.Color.purple()
            )
            embed.set_footer(text=f"Requested by {user.name}",
                             icon_url=user.avatar.url if user.avatar else user.default_avatar.url)

            await ctx.send(embed=embed)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
        finally:
            logger.info('command executed')

    @bot.command(name='cpu-freq')
    async def cpu_fre(ctx):
        try:

            logger.info('Checked CPU frequency')
            user = ctx.author
            cpu_frequency = psutil.cpu_freq()
            embed = discord.Embed(
                description=f'**YOUR CURRENT CPU FREQUENCY**: {cpu_frequency.current}\n **YOUR CPU MAX FREQUENCY**: {cpu_frequency.max}\n **YOUR CPU MIN FREQUENNCY**: {cpu_frequency.min}',
                color=discord.Color.lighter_gray()
            )
            embed.set_footer(text=f"Requested by {user.name}",
                             icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
            await ctx.send(embed=embed)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
        finally:
            logger.info('command executed')

    @bot.command(name='count-cpu')
    async def cc(ctx):
        try:

            logger.info('Checked CPU count')
            user = ctx.author
            cpu = psutil.cpu_count()
            if cpu == 1:
                embed = discord.Embed(
                    title='Total cores your CPU has',
                    description=f'**{cpu}** cores\n\nIt seems like you have a single-core processor. Single-core processors are not that powerful and are not recommended for heavy tasks or gaming. They are good for basic tasks such as *browsing the internet*, *office work*, and *multitasking*. It\'s better to upgrade to a multi-core processor for better performance.'
                )
            elif cpu == 2:
                embed = discord.Embed(
                    title=f'Total cores your CPU has',
                    description=f'**{cpu}** cores\n\nYour CPU is a dual-core processor. Basically dual-core processors are budget level processors and great for everyday tasks such as browsing internet, multitasking, office related work and it can handle low level gaming not ~~much gaming~~ such as low quality graphic games or less demanding games and it\'s provide better performacnce as comapre to single-core processors.',

                )

            elif cpu == 4:
                embed = discord.Embed(
                    title='Total cores your CPU has',
                    description=f'**{cpu}** cores\n\nYour CPU is a quad-core processor. Quad-core processors are great for multitasking, browsing and quite gaming as well as compare to dual-core processors. It can handle some modern or high demanding games and high quality graphic games as well but not at all high quality games only some of them and gaming not at only depend on the CPU it can also depend your others system hardware components. And it\'s provide better performance as compare to dual-core processors.',
                )
            elif cpu == 6:
                embed = discord.Embed(
                    title='Total cores your CPU has',
                    description=f'**{cpu}** cores\n\nYour CPU is a hexa-core processor it\'s sounds nice 🌟. Hexa-core processors well for everything at all, you can perform most them tasks such as all basic task such as *Mutlitasking*, *Offic work*, *Browsing* and etc. And *Gaming* as well as, it can handle most of them modern games with high quality graphics and high demanding games. But other heavy tasks and high end gaming also depend your other system hardware components. '
                )
            elif cpu == 8:
                embed = discord.Embed(
                    title='Total cores your CPU has',
                    description=f'**{cpu}** cores\n\nYour CPU is Octa-core processor it\'s sounds great ❤️‍🔥. Octa-core processors is powerful as compare to hexa-core processors. It\'s provide great performance in most of every taks such as *Multitasking*, *Browsing* and *Gaming*. It can handles heavy games and high demand mdoern games much well *but gaming not at only depends on processor it\'s also depend on your system hardware components*. It\'s really great to have you Octa-core processor.'
                )
            elif cpu >= 12:
                embed = discord.Embed(
                    title='Total cores your CPU has',
                    description=f'**{cpu}** cores\n\nIt seems like you have a high-end processor with 12 cores or more 🔥. These processors are designed for *heavy tasks* and *high-end gaming*. They can handle most of the modern games with high quality graphics and high demanding games, *but gaming not only depends on the processor, it also depends on your other system hardware components*. It\'s really great to have you high-end processor.'
                )
            else:
                embed = discord.Embed(
                    description='It\'s seems like you are not on your system. I can\'t detect your CPU cores :(.',
                )

            embed.set_footer(text=f"Requested by {user.name}",
                             icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
            await ctx.send(embed=embed)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
        finally:
            logger.info('command executed')

    # -------------- http requests handling -----------------------------------------------------------

    @bot.command(name='get', description='Send GET request')
    async def request_send(ctx, url: str):
        user = ctx.author
        Url = url
        req = requests.get(Url)
        try:
            logger.info(f'Sending HTTP request\nRequest url: {url}')
            if req.status_code == 200:
                logger.info(
                    f'Request successful\nRequest code: {req.status_code}'),
                embed = discord.Embed(

                    title='Request sucessfull ✅',
                    description=f'{req.text}\n **Request code**: {req.status_code} ',
                    color=discord.Color.green()
                )
            else:
                logger.error(
                    f'Request failed\nRequest code: {req.status_code}'),
                embed = discord.Embed(
                    title='Request failed :(',
                    description=f'{req.text}\n **Request code**: {req.status_code} ',
                    color=discord.Color.red()
                )
        except requests.exceptions.HTTPError as e:
            logger.error(f"{str(e)}")
            embed = discord.Embed(
                title='Request failed :(',
                description=f'{e}\n **Request code**: {req.status_code} ',
                color=discord.Color.red()
            )
        finally:
            logger.info('command executed')

        embed.set_footer(text=f"Requested by {user.name}",
                         icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
        await ctx.send(embed=embed)

    # ---------- POST request --------------------------------------------------------------------------------

    @bot.command(name='post', description='send POST requests')
    async def post(ctx, url: str, key: str,  data: str):
        user = ctx.author
        req = requests.post(url, data={key: data})
        try:
            logger.info(f'Sending HTTP request\nRequest url: {url}')
            if req.status_code == 200:
                logger.info(
                    f'Request successful\nRequest code: {req.status_code}'),
                embed = discord.Embed(

                    title='Request sucessfull ✅',
                    description=f'{req.text}\n **Request code**: {req.status_code} ',
                    color=discord.Color.green()
                )
            else:
                logger.error(
                    f'Request failed\nRequest code: {req.status_code}'),
                embed = discord.Embed(
                    title='Request failed :(',
                    description=f'{req.text}\n **Request code**: {req.status_code} ',
                    color=discord.Color.red()
                )
        except requests.exceptions.HTTPError as e:
            logger.error(f"{str(e)}")
            embed = discord.Embed(
                title='Request failed :(',
                description=f'{e}\n **Request code**: {req.status_code} ',
                color=discord.Color.red()
            )
        finally:
            logger.info('command executed')

        embed.set_footer(text=f"Requested by {user.name}",
                         icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
        await ctx.send(embed=embed)

    # -------------------------- PUT request ---------------------------------------------------------------

    @bot.command(name='put', description='send PUT requests')
    async def put(ctx, url: str, key: str, data: str):
        user = ctx.author
        req = requests.put(url, data={key: data})
        try:
            logger.info(f'Sending HTTP request\nRequest url: {url}')
            if req.status_code == 200:
                logger.info(
                    f'Request successful\nRequest code: {req.status_code}'),
                embed = discord.Embed(

                    title='Request sucessfull ✅',
                    description=f'{req.text}\n **Request code**: {req.status_code} ',
                    color=discord.Color.green()
                )
            else:
                logger.error(
                    f'Request failed\nRequest code: {req.status_code}'),
                embed = discord.Embed(
                    title='Request failed :(',
                    description=f'{req.text}\n **Request code**: {req.status_code} ',
                    color=discord.Color.red()
                )
        except requests.exceptions.HTTPError as e:
            logger.error(f"{str(e)}")
            embed = discord.Embed(
                title='Request failed :(',
                description=f'{e}\n **Request code**: {req.status_code} ',
                color=discord.Color.red()
            )
        finally:
            logger.info('command executed')

        embed.set_footer(text=f"Requested by {user.name}",
                         icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
        await ctx.send(embed=embed)

    @bot.command(name='bothelp', description='show all available commands')
    async def h(ctx):
        show_commands = """
        **Vector**
        
        This bot is designed to provide fast and accurate information using the **Gemini API** on any topic, along with other powerful features like HTTP requests and fetching your system utilities.
        
        **Bot Name Help Menu**
        Here are the commands you can use with this bot:

    1. **Ask anything**
    
            - `!q [query]`: Ask any question to the bot.
  
        
    2. **HTTP Request Commands**
    
            - `!request-send`: send HTTP request.


    3. **General Utility Commands**
            
            - `!bothelp`: Display this help menu.

        --------------------------------------------------------------------------------

        **How to Use**: 
        - Type `!bothelp [command]` or `/bothelp` to get more detailed information about bot and their commands.

        **Examples**:
        - `!q What is AGI?`: get direct answer.
        
        - `!request-send https://example.com`: Send a HTTP request and show the response.

        Feel free to reach out to the server admins if you need assistance or have any suggestions for new features!

        
        """

        embed = discord.Embed(
            title='Vector help',
            description=show_commands,
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)
