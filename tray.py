from pystray import Icon, Menu, MenuItem
from PIL import Image

def createTrayIcon(onQuit):
    image = Image.open("./images/skip-icon.png")

    return Icon("Spotify Ad Avoider", image, menu=Menu(MenuItem("Quit", onQuit)))