import subprocess

def instalar_pygame():
    try:
        # Ejecutar el comando pip install pygame
        subprocess.check_call(["pip", "install", "pygame"])
        print("Pygame instalado correctamente.")
    except subprocess.CalledProcessError:
        print("Error al instalar Pygame.")

if __name__ == "__main__":
    instalar_pygame()