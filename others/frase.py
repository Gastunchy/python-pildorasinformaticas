import requests

# Colores
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
R = "\033[0m"

url = "https://frasedeldia.azurewebsites.net/api/phrase"

llamada = requests.get(url)

f_llamada = llamada.json()

print(f"\n{CYAN}La frase del dia:{R} \n{GREEN}{f_llamada["phrase"]}")
print(f"\n{CYAN}El autor: \n{GREEN}{f_llamada["author"]}{R}")