"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png"

import requests
import shutil
import json

class Roluxflop:

    def cosa_flop(self):
        r = requests.get(url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.pnnnnnng")
        print(r.content)
        print(r.status_code)

    def flop(self, url, file_name):
        res = requests.get(url,stream=True)

        if 200 == res.status_code:
            with open(file_name, "wb") as f:
                shutil.copyfileobj(res.raw,f)
            print("imagen descarga completamente")
        else:
            print("No se encontro nada")

    def roluxsflop(self,pokemon):
        r = requests.get(url="https://pokeapi.co/api/v2/pokemon/"+pokemon)
        obj = json.loads(r.content)
        return obj["sprites"]["front_shiny"]
    
    pokemon = input("Escoge un pokemon: ")
     
    yoyo = Roluxflop()
    img = yoyo.cosa_flop(pokemon)
    yoyo.roluxs(img, str(pokemon)+".png")