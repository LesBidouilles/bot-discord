"""
on_message functions

ALL functions in this module should be in the form `name(client, message)`
where name is the function's name, client is the Discord client and message is
the message object.

The functions located here will be accessible by calling "prefixname" in a
discord message.
"""
import inspect

import settings


async def count(client, message):
    """
    Compte les messages de la personne qui l'a demandé.

    À cause de limitations dans l'API Discord, est limité aux 100 derniers messages du canal.
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
