import os
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
    
    def openConfigFile(icon, item):
        configFilePath = os.path.abspath("common_ad_names.txt")

        if not os.path.exists(configFilePath):
            print("ERROR - Config file not found.")

        os.startfile(configFilePath)

    return Icon("Spotify Ad Avoider", image, menu=Menu(MenuItem("Spotify Ad Avoider", lambda icon, item: None, enabled=False), Menu.SEPARATOR, MenuItem("Open ad blocker config", openConfigFile), MenuItem("Launch on startup", toggleStartup, checked=checkStartup), MenuItem("Quit", onQuit)))