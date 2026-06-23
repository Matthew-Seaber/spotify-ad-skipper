from pystray import Icon, Menu, MenuItem
from PIL import Image

import startup

def createTrayIcon(onQuit, programPath):
    image = Image.open("./images/skip-icon.png")

    def toggleStartup(icon, item):
        if startup.checkStartupEnabled():
            startup.disableStartup()
        else:
            startup.enableStartup(programPath)

        icon.update_menu()

    def checkStartup(item):
        return startup.checkStartupEnabled()


    return Icon("Spotify Ad Avoider", image, menu=Menu(MenuItem("Launch on startup", toggleStartup, checked=checkStartup), MenuItem("Quit", onQuit)))