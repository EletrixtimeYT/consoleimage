import climage
from PIL import Image
import os
import shutil
import time

# Chemin d'accès au fichier GIF
gif_path = input("Path to gif : ") 

frame_count = 0

def read():
    global frame_count # ajouter cette ligne pour utiliser la variable globale 'frame_count'
    while True:
        if maximage == frame_count:
            print("Finished !")
            shutil.rmtree("decomposed")
            os._exit(0)

        output = climage.convert(f"decomposed/image{frame_count}.png", is_unicode=True)
        print(output)
        
        frame_count += 1
        print(frame_count)
        time.sleep(0.255)
        os.system('clear')

def initread():
    print("Playing gif in the console...")
    read()

# Charger le fichier GIF
gif_file = Image.open(gif_path)

# Créer un dossier pour stocker les images décomposées et supprimer s'il existe
if os.path.exists("decomposed"):
    shutil.rmtree("decomposed")
os.makedirs("decomposed")

# Décomposer le GIF en images individuelles et les enregistrer dans le dossier 'decomposed'
frame_count = 0
maximage = 0
delay_time = 0.1 # Durée d'affichage de chaque image
if 'duration' in gif_file.info:
    delay_time = gif_file.info['duration'] * 0.001 / gif_file.n_frames # Calculer le temps entre chaque image
try:
    while True:
        gif_file.seek(frame_count)
        gif_file.save(f"decomposed/image{frame_count}.png")
        frame_count += 1
        maximage += 1
except EOFError:
    pass

print(f"Le fichier GIF a été décomposé en {frame_count} images.")
frame_count = 0
initread()
