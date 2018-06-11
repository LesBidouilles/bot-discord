import asyncio
import discord
import inspect

import settings
import onMessage


client = discord.Client()

onMessageFunctions = inspect.getmembers(onMessage, inspect.isfunction)


@client.event
async def on_ready():
    """
    Runs when the connexion to Discord is made and ready.
    """
    await client.edit_profile(username="Bidouilleur")

    game = discord.Game(name=settings.RICH_PRESENCE_TEXT)
    await client.change_presence(game=game)

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    """
    Runs whenever a message is posted in an accessible channel for the bot.
    """
    if message.content.startswith(settings.PREFIX):
        msg_content = message.content[1:]
        for name, func in onMessageFunctions:
            if msg_content.startswith(name):
                await func(client, message)


async def init(loop):
    await client.start(settings.BOT_TOKEN)


async def exit(loop):
    await client.logout()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(init(loop))
    except:
        loop.run_until_complete(exit(loop))
    finally:
        loop.close()
