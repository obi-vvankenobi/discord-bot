import discord
from discord.ext import commands
from config import settings
import os
import random

Bot = commands.Bot(command_prefix = settings['prefix'])

client = discord.Client()
@Bot.event
async def on_ready():
    print('Bot is online')


@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')

@Bot.command()
async def ping(ctx):
    ping_ = Bot.latency
    ping = round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")

@Bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    if channel:
        print(channel.id)
        await channel.connect(reconnect=False)
    else:
        await ctx.send('bruh you arent in a vc')

a = ['гей', 'бля', 'заебал', 'сука', 'пизда']
b = ['извини', 'Извини', 'Извени', 'извени']
Predupr = [
        'Еще раз я услышу это слово, засуну тебе его в ASS.',
        'Харе материться, заебал.',
        'Лесные твари, не будьте как твари.',
        'За мат извинись.']
Izvini = ['Нюхай бэбру, пёс']
@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    else:
        content = message.content.split()
        for word in content:
            if word in b:
                await message.channel.send(f'{message.author.mention}')
                await message.channel.send(str(Izvini))
        for word in content:
            if word in a:
                response = random.choice(Predupr)
                await message.channel.send(f'{message.author.mention}')
                await message.channel.send(response)
    await Bot.process_commands(message)

@Bot.command()
async def info(ctx, member:discord.Member):
    emb = discord.Embed(title='Information', color=0xff0000)
    emb.add_field(name='Joined in:', value=member.joined_at, inline=False)
    emb.add_field(name='Name:', value=member.display_name, inline=False)
    emb.add_field(name='User ID:', value=member.id, inline=False)
    emb.add_field(name='Account was created:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC '), inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f'Caused: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=emb)
# @Bot.command()
# async def fox(ctx):
#     response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
#     json_data = json.loads(response.text) # Извлекаем JSON
#
#     embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
#     embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
#     await ctx.send(embed = embed) # Отправляем Embed
token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))