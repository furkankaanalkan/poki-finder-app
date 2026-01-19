import requests
import tkinter

window = tkinter.Tk()
window.title("Poki Finder")
window.geometry("900x700")



foto_label = tkinter.Label(window, image=)
foto_label.pack()










POKE_NAMES = ""

def make_request(url):
    response = requests.get(url)
    return response.json()

#print(make_request("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"))


user_input = 'snorlax' #input("enter poki class: ")



def find_names_urls():
    global POKE_NAMES
    poki_response = make_request("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    for poki in poki_response:
        if poki == "results":
            for index in poki_response["results"]:
                if index["name"] == user_input:
                    POKE_NAMES =  index["url"]
    return

#print(find_names_urls())

def poki_ab():
    empy_list = []
    poke_names_response = make_request(POKE_NAMES)
    for poke in poke_names_response:
        if poke == "abilities":
            for poke in poke_names_response["abilities"]:
                A = poke["ability"]["name"]
                empy_list.append(A)

    return empy_list

def poki_foto():
    poke_names_response = make_request(POKE_NAMES)
    return (poke_names_response['sprites']['front_default'])



#print(poki_ab())
#print(poki_foto())





window.mainloop()