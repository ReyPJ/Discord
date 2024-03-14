from random import choice


def get_responses(user_input: str) -> str:
    name_responses = {
        'gaeso': [
            'Gaeso es puto',
            'Mira Gaeso un turco',
            'Como te van a hackear la cuenta Gaeso xD'
        ],
        'benji': [
            'Benji eres un pendejo',
            'Benji eres un estupido bastardo',
            'Benji tienes cara de nalga',
            'Benji de seguro vives en el cocho',
            'Benji eres un negro',
            'Benji eres un gei lesbiano',
            'Benji eres  judas',
            'Benji eres un cabeza de cebolla',
            'Benji eres un pedo de rata',
            'Benji no es mi culpa que aigas nacido negro'
        ],
        'pae': [
            'Pae eres un pendejo',
            'Pae eres un estupido bastardo',
            'Pae tienes cara de nalga',
            'Pae de seguro vives en el cocho',
            'Pae eres un negro',
            'Pae eres un gei lesbiano',
            'Pae eres  judas',
            'Pae eres un cabeza de cebolla',
            'Pae eres un pedo de rata',
            'Pae no es mi culpa que aigas nacido negro'
        ],
        'mclovin': [
            'Mclovin eres un pendejo',
            'Mclovin eres un estupido bastardo',
            'Mclovin tienes cara de nalga',
            'Mclovin de seguro vives en el cocho',
            'Mclovin eres un negro',
            'Mclovin eres un gei lesbiano',
            'Mclovin eres  judas',
            'Mclovin eres un cabeza de cebolla',
            'Mclovin eres un pedo de rata',
            'Mclovin no es mi culpa que aigas nacido negro'
        ],
        'runas': [
            'https://www.deeplol.gg/champions?version=14.5&tier=Challenger+'
        ]
    }

    lowered = user_input.lower()
    if lowered in name_responses:
        return choice(name_responses[lowered])
    else:
        return 'Callate'
