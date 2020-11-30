import random
from time import sleep
import discord
import requests
from discord.ext import commands


TOKEN = ''
client = commands.Bot(command_prefix='.')


# /\\\\\\\\/
# /\3V3N7S/\
# /\\\\\\\\/


@client.event
async def on_ready():
    print('Bot is online.')


# \\\\\\\\\\\\\\\\\\/
# /\C0MM0N C0MM4NDS/\
# \\\\\\\\\\\\\\\\\\/


@client.command()
async def echo(ctx, *, content: str):
    await ctx.send(content)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send('Target Neutralized :gun:')


@client.command()
async def kick(ctx, member: discord.Member, reason=None):
    await member.kick(reason=reason)
    await ctx.send('Good riddance I say')


@client.command()
async def ban(ctx, member: discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send(" Stop right there criminal scum, you violated the law! now off to jail with ya! ")


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} has been bailed out of jail.')
            return


@client.command()
async def hi(ctx):
    await ctx.send('Hello!')


@client.command()
async def monkey(ctx):
    await ctx.send('https://imgur.com/gallery/R7CmxrT')


@client.command()
async def cmds(ctx):
    embed = discord.Embed(Title='Welcome to Infinity!', description='Just some commands for you.',
                          color=discord.Colour.red())
    embed.add_field(name='.clear',
                    value='Clears at least 5 messages from the current channel unless a number is specified')
    embed.add_field(name='.monkey', value="Sends a picture of a monkey wearing a furry coat...idk why don't ask.")
    embed.add_field(name='.keanu', value='Sends a random meme of Keanu Reeves')
    await ctx.send(content=None, embed=embed)


@client.command()
async def keanu(ctx):
    images = ['https://i.chzbgr.com/full/9320452608/h8EB33011/',
              'https://i.chzbgr.com/full/9320454144/h9A989108/',
              'https://i.chzbgr.com/full/9320455424/hC497C3CD/',
              'https://i.chzbgr.com/full/9320483072/hC7341071/',
              'https://pics.me.me/5-year-old-me-waiting-for-my-parents-to-stop-58726090.png',
              'https://i.redd.it/tqj0yg9e8u431.jpg',
              ]
    await ctx.send(random.choice(images))


@client.command()
async def cat(ctx):
    await ctx.send('https://i.kym-cdn.com/photos/images/newsfeed/001/505/718/136.jpg')


@client.command()
async def darkjoke(ctx):
    response = requests.get('https://sv443.net/jokeapi/category/Dark')
    if response.json()["type"] == "twopart":
        await ctx.channel.send(response.json()["setup"]); sleep(3)
        await ctx.channel.send(response.json()["delivery"])
    elif response.json()["type"] == "single":
        await ctx.channel.send(response.json()["joke"])


@client.command()
async def anyjoke(ctx):
    response = requests.get('https://sv443.net/jokeapi/category/any')
    if response.json()["type"] == "twopart":
        await ctx.channel.send(response.json()["setup"]); sleep(3)
        await ctx.channel.send(response.json()["delivery"])
    elif response.json()["type"] == "single":
        await ctx.channel.send(response.json()["joke"])


# /\//////////////\
# /\V0iCE R3l4ted/\
# /\//////////////\


@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send("H3110! :)")


@client.command()
async def leave(ctx):
    channel = ctx.message.guild.voice_client
    await channel.disconnect()
    await ctx.send("G00dbye! :)")


# /\\\\\\\/
# /\T0KEN/\
# /\\\\\\\/


client.run(TOKEN)
