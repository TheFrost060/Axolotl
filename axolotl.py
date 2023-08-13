import discord
from discord.ext import commands, tasks
# import youtube_dl
import requests
from random import choice


def run_bot():
    TOKEN=''

    intents= discord.Intents.all()
    # intents.message_content = True

    # client = discord.Client()
    bot = commands.Bot(command_prefix='axo ',intents=intents)


    @bot.event
    async def on_ready():
        # Setting `Playing ` status
        # await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Hello World! {axo help}"))

        # Setting `Streaming ` status
        # await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="My Stream", url="my_twitch_url"))

        # Setting `Listening ` status
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="**axo help**"))

        # Setting `Watching ` status
        # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mom"))
        
        print('READY!')

    # status = ['Lost in the fucking world', 'Lofi beats', 'Sleeping', 'Universal chaos']
    # @tasks.loop(seconds=5)
    # async def change_status():
    #     await bot.change_presence(activity=discord.Game(choice(status)))
    # @bot.event
    # async def on_message(message):
    #     if  message.author == bot.user:
    #         return

    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)

    #     print(f"{username} said: '{user_message}' ({channel})")


    @bot.command(name='ping', help='This command returns latency', pass_context=True)
    async def ping(ctx):
        await ctx.channel.send(f'**Pong!** Latency= {round(bot.latency* 1000)}ms')

    @bot.command(name='ILoveYou', help='This command returns a random love message')
    async def hello(ctx):
        responses=['***blushes*** I love you too', 'You already are in my heart :relieved:', 'I love the way you lie :blush:', 'May GOD love you too', 'Heyyy honeybooo!! :heart_eyes:']
        await ctx.send(choice(responses))

    # @bot.command(name='kaushik', help='This command angers the bot')
    # async def hello(ctx):
    #     responses=['***grunts*** tor baba kaushik sala!!']
    #     await ctx.send(choice(responses))

    @bot.command(name='boobies', help='This command returns boobies')
    @commands.is_nsfw()
    async def boobies(ctx):
        em = discord.Embed()
        
        def case1():
            r = requests.get("http://api.nekos.fun:8080/api/boobs")
            res = r.json()
            em.set_image(url = res['image'])
            return em

        def case2():
            r = requests.get("https://api.waifu.im/search/?included_tags=milf")
            res = r.json()
            em.set_image(url = res['images'][0]['url'])
            return em
        
        def case3():
            r = requests.get("http://api.nekos.fun:8080/api/boobs")
            res = r.json()
            em.set_image(url = res['image'])
            return em
        
        await ctx.send(embed = choice([case1(),case2(),case3()]))

    @bot.command(name='waifu', help='This command returns a random waifu image')
    async def waifu(ctx):
        r = requests.get("https://api.waifu.im/search/?included_tags=waifu")
        res = r.json()
        em = discord.Embed()
        em.set_image(url = res['images'][0]['url'])
        await ctx.send(embed = em)

    @bot.command(name='spank', help='This command returns a butt spank')
    async def spank(ctx):
        r = requests.get("http://api.nekos.fun:8080/api/spank")
        res = r.json()
        em = discord.Embed()
        em.set_image(url = res['image'])
        await ctx.send(embed = em)
    
    @bot.command(name='bbjob', help='This command returns boobjob')
    async def waifu(ctx):
        r = requests.get("https://api.waifu.im/search/?included_tags=paizuri")
        res = r.json()
        em = discord.Embed()
        em.set_image(url = res['images'][0]['url'])
        await ctx.send(embed = em)
    
    @bot.command(name='erotic', help='This command returns an erotic image')
    async def waifu(ctx):
        r = requests.get("https://api.waifu.im/search/?included_tags=ero")
        res = r.json()
        em = discord.Embed()
        em.set_image(url = res['images'][0]['url'])
        await ctx.send(embed = em)

    @bot.command(name='sclgrl', help='This command returns an image of a schoolgirl')
    async def waifu(ctx):
        r = requests.get("https://api.waifu.im/search/?included_tags=uniform")
        res = r.json()
        em = discord.Embed()
        em.set_image(url = res['images'][0]['url'])
        await ctx.send(embed = em)

    @bot.command(name='avatar', help='This command returns avatar of a user')
    async def avatar(ctx, member: discord.Member):
        show_avatar = discord.Embed(color= discord.Color.dark_gold())
        show_avatar.set_image(url='{}'.format(member.avatar))
        await ctx.send(embed=show_avatar)
    
    @bot.command(name="profile", help='This command returns profile description of a user')
    async def profile(ctx, member: discord.Member=None):
        if member == None:
            member = ctx.message.author
        inline = True
        embed=discord.Embed(title=member.name+"#"+member.discriminator, color=discord.Color.teal())
        userData = {
            "Mentioned by" : ctx.message.author.mention, #member.mention,
            "Nickname" : member.nick,
            "Member since" : member.created_at.strftime("%b %d, %Y, %T"),
            "Joined at" : member.joined_at.strftime("%b %d, %Y, %T"),
            "Server" : member.guild,
            "Top role" : member.top_role
        }
        for [fieldName, fieldVal] in userData.items():
            embed.add_field(name=fieldName+":", value=fieldVal, inline=inline)
        embed.set_footer(text=f"id: {member.id}")
        
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
    
    
    
    
    
    
    
    
    
    
    #     if user_message[0] == '?':
    #         user_message = user_message[1:]
    #         await send_message(message, user_message, is_private=True)
    #     else:
    #         await send_message(message, user_message, is_private=False)
    bot.run(TOKEN)

