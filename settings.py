from os import environ as environment

# The bot's prefix
PREFIX = "*"

# The Rich Presence text
# Will be displayed as the bot's status message
RICH_PRESENCE_TEXT = "Bot Intelligent De l'Organisation Universelle "\
    "Indépendamment Libre et de L'Entraide Ultra Rapide"

# The header of the help message
HELP_MESSAGE_INTRO = "Salut, le préfixe est `{}`. Voilà les commandes que je "\
    "connais :\n".format(PREFIX)

# The footer of the help message
HELP_MESSAGE_OUTRO = ""

# env variables proxying
# these are defined in the `.env` file which is described in the env file
BOT_TOKEN = environment['BOT_TOKEN']
DATABASE = {
    'host': environment.get('DB_HOST', '127.0.0.1'),
    'user': environment.get('DB_USER', 'postgres'),
    'password': environment.get('DB_PASSWORD', ''),
    'database': environment.get('DB_NAME', 'bot_discord')
}
