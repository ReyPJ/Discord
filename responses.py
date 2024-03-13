from random import choice


def get_responses(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'gaeso':
        return choice(['Gaeso es puto', 'Mira Gaeso un turco', 'Como te van a hackear la cuenta Gaeso xD'])

    elif lowered == 'benji' or lowered == 'pae' or lowered == 'mclovin':
        return choice(
            [
                'pendejo',
                'estupido bastardo',
                'cara de nalga',
                'de seguro vives en el cocho',
                'negro', 'gei lesbiano',
                'judas',
                'cabeza de cebolla',
                'pedo de rata',
                'no es mi culpa que aigas nacido negro'
            ])
