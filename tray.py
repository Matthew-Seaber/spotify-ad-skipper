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
        appDataPath = os.getenv("APPDATA") or os.path.expanduser("~")
        folderPath = os.path.join(appDataPath, "SpotifyAdAvoider")
        os.makedirs(folderPath, exist_ok=True)
        configFilePath = os.path.join(folderPath, "common_ad_names.txt")

        if not os.path.exists(configFilePath):
            print("ERROR - Config file not found")
            return

        os.startfile(configFilePath)

    def resetConfigFile(icon, item):
        appDataPath = os.getenv("APPDATA") or os.path.expanduser("~")
        folderPath = os.path.join(appDataPath, "SpotifyAdAvoider")
        os.makedirs(folderPath, exist_ok=True)
        
        commonAdFilePath = os.path.join(folderPath, "common_ad_names.txt")

        with open(commonAdFilePath, "w") as file:
            file.write("Advertisement\n")
            file.write("LISTEN NOW\n")
            file.write("—\n")
            file.write("Listen to music, ad-free.\n")

    return Icon("Spotify Ad Avoider", image, menu=Menu(MenuItem("Spotify Ad Avoider", lambda icon, item: None, enabled=False), Menu.SEPARATOR, MenuItem("Launch on startup", toggleStartup, checked=checkStartup), MenuItem("Open ad blocker config", openConfigFile), MenuItem("Reset config file", resetConfigFile), Menu.SEPARATOR, MenuItem("Quit", onQuit)))