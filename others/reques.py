import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Ingrese su pokemon: ")

consulta = requests.get(url + pokemon).json()

# Guardar la consulta en un archivo JSON
with open(f"{pokemon}.json", "w") as archivo:
    json.dump(consulta, archivo, indent=4)

print(f"Consulta guardada en {pokemon}.json")