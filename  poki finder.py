import requests
import json



def make_request():
    response = requests.get(url="https://pokeapi.co/api/v2/pokemon/ditto")
    return response.json()


print(make_request())