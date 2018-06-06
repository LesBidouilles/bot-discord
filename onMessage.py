"""
on_message functions

ALL functions in this module should be in the form `name(client, message)`
where name is the function's name, client is the Discord client and message is
the message object.

The functions located here will be accessible by calling "prefixname" in a
discord message.
"""
import asyncio
import discord
import inspect

import settings
import utils


async def count(client, message):
    """
    Compte les messages de la personne qui l'a demandé.

    À cause de limitations dans l'API Discord, est limité aux 100 derniers
    messages du canal.
    """
    counter = 0
    tmp = await client.send_message(message.channel, 'Calculating messages...')

    async for log in client.logs_from(message.channel, limit=100):
        if log.author == message.author:
            counter += 1

    await client.edit_message(tmp, 'You have {} messages.'.format(counter))


async def help(client, message):
    """
    Aide à propos des fonctions supportées.
    """
    # gets all current module's functions
    functions = inspect.getmembers(__import__(__name__), inspect.isfunction)

    answer = settings.HELP_MESSAGE_INTRO

    for name, function in functions:
        answer += "`{}` : {}\n".format(name, function.__doc__)

    answer += settings.HELP_MESSAGE_OUTRO

    await client.send_message(message.channel, answer)


async def tempmute(client, message):
    """
    Mute la personne mentionnée pendant un certain temps.

    Prototype: "tempmute @user [@user ...] temps"
    Avec le temps "1h 1m 1s"

    Exemples: "tempmute @someone 1m"
    "tempmute @one @two 1h 1m 1s"
    """
    msg_channel = message.channel
    author = message.author

    if msg_channel.permissions_for(author).manage_messages:
        time = utils.parseTime(message.content)

        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.speak = False

        output_msg = ""

        for member in message.mentions:
            output_msg += "{} ".format(member.mention)
            for channel in msg_channel.server.channels:
                await client.edit_channel_permissions(channel, member,
                                                      overwrite)

        output_msg += "a été rendu muet pour {} secondes".format(time)

        await client.send_message(msg_channel, output_msg)

        await asyncio.sleep(time)

        for member in message.mentions:
            for channel in msg_channel.server.channels:
                await client.delete_channel_permissions(channel, member)
