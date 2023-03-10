import discord
import re

TOKEN = 'your_bot_token_here'
# Replace with the ID of the source channel
SOURCE_CHANNEL_ID = 123456789012345678
# Replace with the ID of the destination channel
DESTINATION_CHANNEL_ID = 123456789012345679

platforms = [
    'www.youtube.com',
    'm.youtube.com',
    'music.youtube.com',
    'youtu.be',
    'open.spotify.com',
    'play.spotify.com',
    'embed.spotify.com',
    'api.spotify.com',
    'soundcloud.com',
    'on.soundcloud.com',
    'api.soundcloud.com',
    'm.soundcloud.com',
    'music.apple.com',
    'itunes.apple.com',
    'listen.tidal.com',
    'my.tidal.com',
    'video.tidal.com',
    'music.amazon.com',
    'www.amazon.com/music',
    'pandora.com',
    'pdora.co',
    'www.deezer.com',
    'api.deezer.com',
    'deezer.com',
]

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online.')


@bot.command(name='transfer')
async def transfer(ctx):
    source_channel = bot.get_channel(SOURCE_CHANNEL_ID)
    destination_channel = bot.get_channel(DESTINATION_CHANNEL_ID)

    pattern = re.compile(r'(https?://\S+)')
    async for message in source_channel.history(limit=None):
        for match in pattern.findall(message.content):
            if match.endswith('.mp3'):
                await destination_channel.send(match)
            else:
                domain = match.split('/')[2]
                if domain in platforms:
                    await destination_channel.send(match)

    await ctx.send('All links transferred successfully!')

bot.run(TOKEN)
