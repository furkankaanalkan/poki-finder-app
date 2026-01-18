import requests
import json



def make_request(url):
    response = requests.get(url)
    return response.json()

print(make_request("https://pokeapi.co/api/v2/pokemon/ditto"))


poki_response = make_request("https://pokeapi.co/api/v2/pokemon/ditto")

#user_input = input("enter poki class: ")
for poki in poki_response:
    if poki == "game_indices":
        for index in poki_response["game_indices"]:
            print(index)




