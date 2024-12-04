#Botto by Gytis5089

import discord.utils
import discord
import asyncio
import random
import os
from discord_buttons import DiscordButton, Button, ButtonStyle, InteractionType
from discord.ext import commands
from discord.utils import get
from discord.ext import menus
os.chdir("D:\Botto")

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())
client.remove_command('help')
ddb = DiscordButton(client)

def is_gytis(ctx):
    return ctx.author.id in [301014178703998987]
#Me

def access(ctx):
    return ctx.author.id in [301014178703998987, 667029055727599627, 505544793477087242, 701035026841600024]
#Me, EpicOverlord, Levski, Fydro

@client.event
async def on_ready():
    thebasement = client.get_guild(831927083113906237)
    uptimechannel = client.get_channel(844636165608046615)
    await uptimechannel.send("`Botto is now online.`")
    ticketschannel = client.get_channel(832273651645546558)
    overwrites = {
        thebasement.default_role: discord.PermissionOverwrite(
            view_channel=True,
            create_instant_invite=True,
            send_messages=True,
            read_message_history=True
        )
    }
    await ticketschannel.edit(overwrites=overwrites)
    await client.change_presence(activity=discord.Game(name=f"!help"))
    print('Botto now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.event
async def on_message(message):
    category1 = client.get_channel(831965796094967869)
    if message.channel.id == 832273651645546558:
        if message.content in ["create",  "Create"]:
            ID = str(message.author.id)
            channel = get(message.guild.channels, name=ID)
            if channel:
                await message.author.send("Looks like you already have a ticket currently open!")
                await message.delete()
            else:
                overwrites = {
                    message.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    message.author: discord.PermissionOverwrite(read_message_history=True, send_messages=True, view_channel=True)
                }
                await message.guild.create_text_channel(ID, overwrites=overwrites, category=category1)
                embed= discord.Embed(
                    title="Ticket",
                    colour=0x000000,
                    description="Welcome, expect a <@&832268223990857758> to be with you soon.\nPlease do not ping a specific user unless it's really important.\nIf at any time you would like to close this ticket, just say `close`"
                )
                embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
                channel = discord.utils.get(message.guild.channels, name=f"{message.author.id}")
                await channel.send(embed=embed)
                message1 = await channel.send("<@&832268223990857758>")
                message2 = await channel.send(f"{message.author.mention}")
                await message.delete()
                await message1.delete()
                await message2.delete()
    if message.channel.id == 832273651645546558:
        if message.content not in ["create", "Create"]:
            await message.delete()
    if discord.utils.get(message.guild.channels, id=831965796094967869):
        dontdelete = [844636165608046615, 833079663902720031, 831986564716036187, 831986538245783625, 831986522731315212, 832273651645546558, 832275928452694086, 832275957120630825, 832276008953708585, 832276021314584617, 831927084087509065, 831994976456015883, 831927084087509065, 831994976456015883, 832738460263120896, 832735314593316924]
        #Bot-Uptime, Welcome, Rules, Info, Announcements, Tickets, Purgatory Info, Purgatory Chat, Suspended Info, Suspended Chat, General, Bot Commands, Mods, Logs
        if message.channel.id not in dontdelete:
            if message.content in ["close", "Close"]:
                await message.channel.send("Closing..")
                await asyncio.sleep(5)
                await message.channel.delete()
    if message.author.id in [301014178703998987, 667029055727599627, 505544793477087242, 701035026841600024]:
        if discord.utils.get(message.guild.channels, id=831965796094967869):
            if message.content in ["claim", "Claim"]:
                if message.channel.topic == None:
                    logs = client.get_channel(832735314593316924)
                    await logs.send(f"{message.author.mention} has claimed {message.channel.mention}")
                    await message.channel.edit(topic=f"{message.author.id}")
                    await message.channel.send(f"{message.author.mention} has successfully claimed this ticket")
                elif message.channel.topic == str(message.author.id):
                    await message.channel.send(f"Uh-oh {message.author.mention}, looks like you've already claimed this ticket")
                else:
                    await message.channel.send(f"Sorry, this ticket has already been claimed by <@{message.channel.topic}>")
    await client.process_commands(message)

@client.command()
async def buttontest(ctx):
    m = await ctx.send(
        "Content",
        buttons=[
            Button(style=ButtonStyle.blue, label="Blue"),
            Button(style=ButtonStyle.red, label="Red"),
            Button(style=ButtonStyle.URL, label="url", url="https://example.org"),
        ],
    )

    res = await ddb.wait_for_button_click(m)
    await res.respond(
        type=InteractionType.ChannelMessageWithSource,
        content=f'{res.button.label} clicked'
    )

@client.command(aliases=['purge', 'wipe'])
@commands.check(access)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title = 'Wipe',
        colour = 0x000000,
        description = f'{ctx.author.mention} has wiped {amount} messages'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has wiped {amount} messages in {ctx.channel.mention}")

@client.command()
@commands.check(access)
async def warn(ctx, member : discord.Member, *, arg=None):
    if arg == "":
        arg == "N/A"
    embed = discord.Embed(
        title = 'Warn',
        colour = 0x000000,
        description = f'{ctx.author.mention} has warned {member.mention} for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    embed = discord.Embed(
        title = 'Kick',
        colour = 0x000000,
        description = f'{ctx.author.mention} has warned you for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await member.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has warned {member.mention} for:\n{arg}")

@client.command()
@commands.check(access)
async def kick(ctx, member : discord.Member, *, arg=None):
    embed = discord.Embed(
        title = 'Kick',
        colour = 0x000000,
        description = f'{ctx.author.mention} has kicked <@{member.id}> for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    embed = discord.Embed(
        title = 'Kick',
        colour = 0x000000,
        description = f'{ctx.author.mention} has kicked you for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await member.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has kicked {member.mention} for:\n{arg}")
    await member.kick(reason=arg)

@client.command()
@commands.check(access)
async def ban(ctx, member : discord.Member, *, arg=None):
    if arg == "":
        arg == "N/A"
    embed = discord.Embed(
        title = 'Ban',
        colour = 0x000000,
        description = f'{ctx.author.mention} has banned <@{member.id}> for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    role = ctx.guild.get_role(832261594419167273)
    await member.add_roles(role)
    embed = discord.Embed(
        title = 'Ban',
        colour = 0x000000,
        description = f'{ctx.author.mention} has banned you for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await member.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has banned {member.mention} for:\n{arg}")

@client.command()
@commands.check(access)
async def unban(ctx, member : discord.Member):
    embed = discord.Embed(
        title = 'Unban',
        colour = 0x000000,
        description = f'{ctx.author.mention} has banned unanned <@{member.id}>'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    role = ctx.guild.get_role(832261594419167273)
    await member.remove_roles(role)
    embed = discord.Embed(
        title = 'Unban',
        colour = 0x000000,
        description = f'{ctx.author.mention} has unbanned you'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await member.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has unbanned {member.mention}")

@client.command()
@commands.check(access)
async def suspend(ctx, member : discord.Member = None, *, arg=None):
    embed = discord.Embed(
        title = 'Suspend',
        colour = 0x000000,
        description = f'{ctx.author.mention} has suspended <@{member.id}> for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    role = ctx.guild.get_role(832261568074088468)
    await member.add_roles(role)
    embed = discord.Embed(
        title = 'Suspend',
        colour = 0x000000,
        description = f'{ctx.author.mention} has suspended you for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await member.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has suspended {member.mention} for:\n{arg}")

@client.command()
@commands.check(access)
async def unsuspend(ctx, member : discord.Member = None):
    embed = discord.Embed(
        title = 'Unsuspend',
        colour = 0x000000,
        description = f'{ctx.author.mention} has unsuspended <@{member.id}>'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    role = ctx.guild.get_role(832261568074088468)
    await member.remove_roles(role)
    embed = discord.Embed(
        title = 'Unsuspend',
        colour = 0x000000,
        description = f'{ctx.author.mention} has unsuspended you'
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await member.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has unsuspended {member.mention}")

@client.command()
async def appeal(ctx, *, arg):
    gytis = client.get_user(301014178703998987)
    ID = str(ctx.author.id)
    try:
        f = open(f"APPEAL{ID}.txt", "x")
        f.write(arg)
        await gytis.send("An appeal has been made under the name " + ID)
        embed  = discord.Embed(
            title='Appeal',
            colour=0x000000,
            description=f"{arg}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
        await ctx.author.send(embed=embed)
        await ctx.send("Appeal sent.")
    except:
        await ctx.send("Sorry, you have already made an appeal and are therefore not permitted to create a new one.\nIf you believe this is incorrect, please contact a bot developer to fix the bug or clear your appeal.")

@client.command()
@commands.check(access)
async def appealclear(ctx, member : discord.Member):
    ID = str(member.id)
    try:
        filelocation = f"D:\Botto\APPEAL{ID}.txt"
        os.remove(filelocation)
        await ctx.send("Cleared.")
    except:
        await ctx.send("Sorry, this user does not currently have an active appeal.\nIf you believe this is incorrect, please contact a bot developer to fix the bug or manually clear the appeal.")
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has cleared {member.mention}'s appeal")

@client.command()
async def apply(ctx, *, arg):
    gytis = client.get_user(301014178703998987)
    ID = str(ctx.author.id)
    try:
        f = open(f"APPLICATION{ID}.txt", "x")
        f.write(arg)
        await gytis.send("An application has been made under the name " + ID)
        embed  = discord.Embed(
            title='Application',
            colour=0x000000,
            description=f"{arg}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
        await ctx.author.send(embed=embed)
        await ctx.send("Application sent.")
    except:
        await ctx.send("Sorry, you have already made an application and are therefore not permitted to create a new one.\nIf you believe this is incorrect, please contact a bot developer to fix the bug or reset your application.")

@client.command()
@commands.check(access)
async def applicationreset(ctx, member : discord.Member):
    ID = str(member.id)
    try:
        filelocation = f"D:\Botto\APPLICATION{ID}.txt"
        os.remove(filelocation)
        await ctx.send("Cleared.")
    except:
        await ctx.send("Sorry, this user does not currently have an active application.\nIf you believe this is incorrect, please contact a bot developer to fix the bug or manually reset the application.")
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has cleared {member.mention}'s application")

@client.command()
@commands.check(is_gytis)
async def mod(ctx, member : discord.Member):
    ID = str(member.id)
    filelocation = f"D:\Botto\APPLICATION{ID}.txt"
    if filelocation:
        os.remove(filelocation)
    else:
        pass
    await ctx.send("Done.")
    role = ctx.guild.get_role(846107891026624522)
    await member.add_roles(role)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has made {member.mention} a Community Moderator")
    await member.send("You are now a The Basement Community Moderator.")

@client.command()
async def modterms(ctx):
    embed = discord.Embed(
        title="Mod Requirements",
        colour=0x000000,
        description="__**Mod Requirements**__\n- Have previous experience in moderating servers.\n- Been a member of this server for at least 1 month.\n- Be a trustworthy member of the community.\n- Be an active member of the server.\n- Obey the server rules and the Discord Terms of Service and Community Guidelines at all times.\n- Be civil and professional at all times."
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await ctx.send(embed=embed)

@client.command(aliases=['member'])
async def members(ctx):
    mc = ctx.guild.member_count
    goal = 50
    close = goal-mc
    embed = discord.Embed(
        title="Server Members",
        colour=0x000000,
        description=f"**Members:**{mc}\n**Goal:**{goal}\n**How Close:**{close}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await ctx.send(embed=embed)

@client.command()
@commands.check(access)
async def nick(ctx, member : discord.Member, *, arg=None):
    colour = ['Blue', 'Yellow', 'Red', 'Green', 'Indigo', 'Teal', 'White', 'Black', 'Orange', 'Violet', 'Purple', 'Pink', 'Silver', 'Gold', 'Beige', 'Brown', 'Gray', 'Aqua', 'Peach']
    animal = ['Dolphin', 'Crab', 'Pony', 'Horse', 'Dog', 'Cat', 'Ant', 'Penguin', 'Bird', 'Fish', 'Bear', 'Tiger', 'Frog', 'Elephant', 'Giraffe', 'Monkey', 'Turtle', 'Wolf', 'Snake', 'Deer', 'Shark']
    newname = (f"{random.choice(colour)}{random.choice(animal)}{random.randrange(0, 100)}")
    await member.edit(nick=newname)
    embed = discord.Embed(
        title="Nick",
        colour=0x000000,
        description=f"A community moderator has requested for you to change your username.\nIf you do not change it within a day, you will be suspended.\nUntil then, your username is now {newname}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await member.send(embed=embed)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has nicked {member.mention} for {arg}")

@client.command()
@commands.check(access)
async def nickreset(ctx, member : discord.Member):
    await member.edit(nick=None)
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has reset {member.mention}'s nick")

@client.command(aliases=["join"])
async def create(ctx, member : discord.Member):
    await ctx.send(f"{member.name} created their account on {str(member.created_at)[0:10]}\nAnd joined the server on {str(member.joined_at)[0:10]}")

@client.command()
@commands.check(access)
async def announce(ctx, *, arg):
	channel = client.get_channel(831986522731315212)
	await channel.send(f'@everyone\n\n**----------**\n\n{arg}\n\n**----------**\n\nAnnouncement by: {ctx.author.mention}')

@client.command()
@commands.check(access)
async def say(ctx, *, arg):
    await ctx.send(arg)

@client.command(aliases=['guilds', 'guild', 'server'])
@commands.check(access)
async def servers(ctx):
    embed = discord.Embed(
        title='Servers',
        colour=0x000000
    )
    for guild in client.guilds:
       embed.add_field(name=guild.name, value=f'`ID:`{guild.id}\n`Members:`{guild.member_count}\n`Owner:`{guild.owner}', inline=False)
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent.')
    channel = client.get_channel(832735314593316924)
    await channel.send(f"{ctx.author.mention} has just requested the bot's server list")

@commands.group(invoke_without_command=True)
async def dcolour(ctx):
    embed = discord.Embed(
        title="Discord Colour Palette",
        colour=0x000000,
        description="Brilliance Red (BRLL)\nHypesquad Yellow (HPSQ)\nBug Hunter Green (BHNT)\nBalance Cyan (BLNC)\nGreyple (GRPL)\nNot Quite Black(NQBL)\nNitro Grey(NTGR)\nPartner Blue (PTNR)\nDark Mode Grey (DGRY)\nDeveloper Blue (DEVL)\nNitro Blue (NRBL)\nBlurple (BLPL)\nDark Blurple (DBPL)\nBravery Purple (BRVY)\nBoost Pink (BSTP)\nFull White (WHTE)"
    )
    embed.add_field(name="Reference")
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")

@dcolour.command()
async def BRLL(ctx):
    embed = discord.Embed (
        title="Brilliance Red",
        colour=0xF47B67,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def HPSQ(ctx):
    embed = discord.Embed (
        title="Hypesquad Yellow",
        colour=0xF8A532,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def BHNT(ctx):
    embed = discord.Embed (
        title="Bug Hunter Green",
        colour=0x48B784,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def BLNC(ctx):
    embed = discord.Embed (
        title="Balance Cyan",
        colour=0x45DDC0,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def GRPL(ctx):
    embed = discord.Embed (
        title="Greyple",
        colour=0x99AAB5,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def NQBL(ctx):
    embed = discord.Embed (
        title="Not Quite Black",
        colour=0x23272A,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def NTGR(ctx):
    embed = discord.Embed (
        title="Nitro Grey",
        colour=0xB7C2CE,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def PTNR(ctx):
    embed = discord.Embed (
        title="Partner Blue",
        colour=0x4187ED,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def DGRY(ctx):
    embed = discord.Embed (
        title="Dark Mode Grey",
        colour=0x36393F,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def DEVL(ctx):
    embed = discord.Embed (
        title="Developer Blue",
        colour=0x3E70DD,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def NRBL(ctx):
    embed = discord.Embed (
        title="Nitro Blue",
        colour=0x4F5D7F,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def BLPL(ctx):
    embed = discord.Embed (
        title="Blurple",
        colour=0x7289DA,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def DBPL(ctx):
    embed = discord.Embed (
        title="Dark Blurple",
        colour=0x4E5D94,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def BRVY(ctx):
    embed = discord.Embed (
        title="Bravery Purple",
        colour=0x9C84EF,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def BSTP(ctx):
    embed = discord.Embed (
        title="Boost Pink",
        colour=0xF47FFF,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@dcolour.command()
async def WHTE(ctx):
    embed = discord.Embed (
        title="Full White",
        colour=0xFFFFFF,
        description=""
    )
    embed.set_thumbnail(url="https://i.redd.it/kc1uyz4qowx61.png")
    await ctx.author.send(embed=embed)

@client.command()
async def gytis(ctx):
    embed = discord.Embed(
        title="Hey, I'm Gytis!",
        colour=0x000000,
        description="Hey, I'm the owner of the server and developer of <@831908223086624768>\nI'm 14 years old based in the United Kingdom :scotland: though, half Lithuanian :flag_lt:\nI do youtube found [here](https://www.youtube.com/channel/UCNn-GJPGyagchk25jGHVtdw)\nI do __paid__ edits for people and much more like GFX and bots!\nIf you ever want to talk to me just `create` a <#832273651645546558>"
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)
    await message.add_reaction("<:Gytis:832744482289483818>")

@client.command()
async def epicoverlord(ctx):
    embed = discord.Embed(
        title="Hey, I'm EpicOverlord!",
        colour=0xff88ff,
        description="Hey there! I am a moderator here, and in other big community servers. I also own a server too!\nI'm 15 years of age, and I live in Scotland. :scotland:\nI make Discord content on YouTube, and my YouTube Channel can be found [here](https://www.youtube.com/channel/UCZ28usi8U7BlghUkt6OqnUA)\nFeel free to ping, DM, or make a ticket if you ever want to talk to me :smile:"
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)

@client.command()
async def levski(ctx):
    embed = discord.Embed(
        title="Hey, I'm Levski!",
        colour=0x4108ff,
        description="Hello There, I am a moderator in this server.\nI'm 14 years old and i live in Scotland :scotland:\nI have a youtube channel where i add some questionable videos every once and a while, you can find it [here](https://www.youtube.com/channel/UCEqAMSg8YKfEC8hGhRSvTEg) \nIf you would like to talk to me, Please DM Me :thumbsup:"
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)

@client.command()
async def fydro(ctx):
    embed = discord.Embed(
        title="Hey, I'm Fydro!",
        colour=0x1005FE,
        description="Hey! My name is Jamie based in the best of the world Scotland. :scotland:\nIm 13 years of age.\nMy hobbies are Boxing and creating content.\nIf ever you need me please reach out to me through priv dms or a ticket. :upside_down:"
    )
    embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
    message = await ctx.send(embed=embed)

@client.command()
@commands.check(access)
async def ticketadd(ctx, member : discord.Member):
    channel = ctx.channel
    guytoadd = member
    overwrites ={
        ctx.guild.default_role: discord.PermissionOverwrite(
            read_messages=False
        ),
        guytoadd: discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            read_message_history=True
        )
    }
    await channel.edit(overwrites=overwrites)

@client.command()
@commands.check(access)
async def ticketremove(ctx, member : discord.Member):
    channel = ctx.channel
    guytoremove = member
    overwrites ={
        ctx.guild.default_role: discord.PermissionOverwrite(
            read_messages=False
        ),
        guytoremove: discord.PermissionOverwrite(
            view_channel=False,
            send_messages=False,
            read_message_history=False
        )
    }
    await channel.edit(overwrites=overwrites)

@client.command()
@commands.check(access)
async def offline(ctx):
    gytis = client.get_user(301014178703998987)
    uptimechannel = client.get_channel(844636165608046615)
    ticketschannel = client.get_channel(832273651645546558)
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(
            view_channel=True,
            create_instant_invite=True,
            send_messages=False,
            read_message_history=True
        )
    }
    await ticketschannel.edit(overwrites=overwrites)
    await uptimechannel.send("`Botto is now offline.`")
    await gytis.send("The server is now set for the bot to go offline.")

class MyMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):
        embed = discord.Embed (
            title="Help",
            colour=0x000000,
            description="Which menu would you like to access?\n"
        )
        embed.add_field(name="\U0001f1f8", value="Standard Help Menu")
        embed.add_field(name="\U0001f1f2", value="Moderator Help Menu")
        embed.add_field(name="\U0001f1f5", value="Private Help Menu")
        embed.add_field(name="Assistance", value="[Here](https://discord.com/channels/831927083113906237/832273651645546558)")
        embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
        return await channel.send(embed=embed)

    @menus.button('\U0001f1f8')
    async def on_standard(self, payload):
        embed = discord.Embed(
            title="Help",
            colour=0x000000,
            description="`!help` - This command\n`!create` - Shows when a user created their account and when they joined the server\n`!appeal` - Allows you to appeal a suspension or ban\n`!apply` - Allows you to apply for Community Moderator (!modterms)\n`!modterms` - Shows the requirements to apply for moderator (!apply)\n`!members` - Check current amount of members\n`!announce` - Drop something in <#831986522731315212>\n`!ticketadd` - Adds the specified user to your ticket\n`!ticketremove` - Removes the specified user from your ticket\n`create` in <#832273651645546558> to create a ticket\n`close` to close your ticket"
        )
        embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
        await self.message.edit(embed=embed)
        self.stop()

    @menus.button('\U0001f1f2')
    async def on_mod(self, payload):
        embed = discord.Embed(
            title="Mod Help",
            colour=0x000000,
            description="`!clear` - Clears specified amount of messages (+1)\n`!warn` - Warn a user for the specified reason O\n`!kick` - Kicks specified user for specified reason O\n`!ban` - Bans specified user for specified reason O\n`!unban` - Unbans specified user\n`!suspend` - Suspends specified user for specified reason O\n`!unsuspend` - Unsuspends the specified user\n`!appealclear` - Clears the specified user's active appeal\n`!applicationreset` - Resets the specified user's active application\n`!nick` - Hides the specified user's nickname for the specified reason O\n`!nickreset` - Resets the specified user's nick\n`!say` - Says what you say\n`!servers` - Sends a list of servers the bot is in\n`!offline` - To be run when the bot is to go down (locks <#832273651645546558> and some other things)\n`claim` - To claim a ticket"
        )
        embed.add_field(name="Key", value="O = Optional")
        embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
        await self.message.edit(embed=embed)
        self.stop()

    @menus.button('\U0001f1f5')
    async def on_private(self, payload):
        embed = discord.Embed(
            title="Private Help",
            colour=0x000000,
            description="`!gytis` - <@301014178703998987>'s introduction\n`!epicoverlord` - <@667029055727599627>'s introduction\n`!levski` - <@505544793477087242>'s introduction\n`!fydro` - <@701035026841600024>'s introduction"
        )
        embed.set_thumbnail(url="https://i.ibb.co/3Srs1pR/PFP.png")
        await self.message.edit(embed=embed)
        self.stop()

@client.command()
async def help(ctx):
    m = MyMenu()
    await m.start(ctx)

client.run('ODMxOTA4MjIzMDg2NjI0NzY4.YHcE6A.cLwzUTHwBBNSpiMGFlMqMojNrVQ')