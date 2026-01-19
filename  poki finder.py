import requests
import tkinter

window = tkinter.Tk()
window.title("Poki Finder")
window.geometry("500x600")






POKE_NAMES = ""


def make_request(url):
    response = requests.get(url)
    return response.json()

make_request("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")

entry_1 = tkinter.Entry(window,font=("Arial", 14))
entry_1.pack(pady=10)
entry_1.pack()






def find_names_urls():
    user_input = entry_1.get()
    global POKE_NAMES
    poki_response = make_request("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    for poki in poki_response:
        if poki == "results":
            for index in poki_response["results"]:
                if index["name"] == user_input.lower():
                    POKE_NAMES =  index["url"]
    return POKE_NAMES


def poki_ab():
    empy_list = []
    poke_names_response = make_request(POKE_NAMES)
    for poke in poke_names_response:
        if poke == "abilities":
            for poke in poke_names_response["abilities"]:
                A = poke["ability"]["name"]
                empy_list.append(A)

    return empy_list

def functions():
    try:
        find_names_urls()
        poki_ab()
        label_2.config(text=f'Abilities : {poki_ab()}', fg="blue", font=("Arial", 15, "bold"))
    except:
        label_2.config(text='No Pokemon Found', fg="red")









or_image = tkinter.PhotoImage(file='snorlax.png')
resized_or_image = or_image.zoom(4,4)
foto_label = tkinter.Label(window, image=resized_or_image, compound="top")
foto_label.pack(pady=10)
foto_label.pack()


button = tkinter.Button(window, text="Find Name", command=functions, font=("Arial", 12))
button.pack()

label_2 = tkinter.Label(window, text='')
label_2.pack()




window.mainloop()