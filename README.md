bot-discord
===========

Bot discord personnalisé pour le serveur [Bidouilleurs et Bidouilleuses](https://discord.gg/zqmTn7S)

## Installation

**Il faut avoir [`git`][git], [`pipenv`][pipenv] et [`python3.6`][python]
installés au préalable.**
La procédure d'installation varie suivant les OS.

```sh
git clone git@github.com:LesBidouilles/bot-discord.git
# ou 
git clone https://github.com/LesBidouilles/bot-discord.git

cd bot-discord

pipenv sync --dev # ou sans --dev si installation en production
```

## Exécution

```sh
pipenv run python main.py token_de_compte_bot
```

## Tests

Il n'y a pas encore de tests unitaires en place, donc les seuls tests à exécuter
sont les vérifications pep8.

```sh
pipenv run flake8  # si il n'y a rien, c'est bon
pipenv check
```

[git]: https://git-scm.com
[pipenv]: https://pypi.org/project/pipenv/
[python]: https://www.python.org
