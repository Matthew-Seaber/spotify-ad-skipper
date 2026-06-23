import os
from pystray import Icon, Menu, MenuItem
from PIL import Image

import startup

def createTrayIcon(onQuit, programPath):
    imagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "skip-icon.png")
    image = Image.open(imagePath)

    def toggleStartup(icon, item):
        if startup.checkStartupEnabled():
            startup.disableStartup()
        else:
            startup.enableStartup(programPath)

        icon.update_menu()

    def checkStartup(item):
        return startup.checkStartupEnabled()
    
    def openConfigFile(icon, item):
        configFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "common_ad_names.txt")

        if not os.path.exists(configFilePath):
            print("ERROR - Config file not found.")

        os.startfile(configFilePath)

    return Icon("Spotify Ad Avoider", image, menu=Menu(MenuItem("Spotify Ad Avoider", lambda icon, item: None, enabled=False), Menu.SEPARATOR, MenuItem("Open ad blocker config", openConfigFile), MenuItem("Launch on startup", toggleStartup, checked=checkStartup), MenuItem("Quit", onQuit)))