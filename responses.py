from random import choice


def get_responses(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'gaeso':
        return choice(['Gaeso es puto', 'Mira gaeso un turco', 'Como te van a hackear la cuenta xD'])