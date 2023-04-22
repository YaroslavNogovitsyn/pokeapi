import requests
import pprint


def pars(name='pikachu'):
    URL = f'https://pokeapi.co/api/v2/pokemon/{name}'
    params = {}
    response = requests.get(URL, params=params)
    result = response.json()
    return result


class Pokemon:
    def __init__(self, name='ditto'):
        sl = pars(name)
        self.weight = sl['weight']
        self.height = sl['height']
        self.type = sl['types'][0]['type']['name']
        self.id = sl['id']
        self.base_expirience = sl['base_experience']
        self.stats = sl['stats']


if __name__ == '__main__':
    pokemon = Pokemon()
    print(pokemon.stats)
