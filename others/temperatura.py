from clave import key
import requests
from tkinter import messagebox

ciudad = input("Ingrese ciudad: ").lower()

url = "https://api.weatherapi.com/v1/current.json"

respuesta = requests.get(f"{url}?key={key}&q={ciudad}")

json = respuesta.json()

ciudad_nombre = json["location"]["name"]
temperatura = json["current"]["temp_c"]
humedad = json["current"]["humidity"]
region = json["location"]["region"]

print(f" Ciudad: {ciudad_nombre}    \
      \n Temperatura: {temperatura}°C  \
      \n Humedad: {humedad} \
      \n Region: {region}")


# Customizado por chatgpt para ponerle imagen
""" import tkinter as tk
from tkinter import messagebox
import requests
from clave import key

# Función para obtener el clima de la ciudad
def obtener_clima():
    ciudad = entry_ciudad.get().lower()
    url = "https://api.weatherapi.com/v1/current.json"
    
    try:
        respuesta = requests.get(f"{url}?key={key}&q={ciudad}")
        respuesta.raise_for_status()  # Levanta un error si la solicitud no fue exitosa
        datos = respuesta.json()
        
        clima = datos["current"]
        mostrar_clima(clima)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error de red", f"No se pudo obtener la información del clima: {e}")
    except KeyError:
        messagebox.showerror("Error", "No se encontró información del clima para la ciudad ingresada.")

# Función para mostrar el clima en un cuadro de mensaje
def mostrar_clima(clima):
    mensaje = (
        f"Temperatura: {clima['temp_c']}°C\n"
        f"Condición: {clima['condition']['text']}\n"
        f"Humedad: {clima['humidity']}%\n"
        f"Viento: {clima['wind_kph']} kph"
    )
    messagebox.showinfo("Clima Actual", mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Consulta de Clima")

# Crear y colocar los widgets
label_ciudad = tk.Label(ventana, text="Ingrese ciudad:")
label_ciudad.pack(pady=10)

entry_ciudad = tk.Entry(ventana)
entry_ciudad.pack(pady=5)

boton_consultar = tk.Button(ventana, text="Consultar Clima", command=obtener_clima)
boton_consultar.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop() """
