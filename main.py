import asyncio
import threading
import sys
import os
import win32event
import win32api
import winerror

from spotify import restartSpotify, getSongTitle
from tray import createTrayIcon

running = True
commonAdNames = []

async def program():
    appDataPath = os.getenv("APPDATA") or os.path.expanduser("~")
    folderPath = os.path.join(appDataPath, "SpotifyAdAvoider")
    os.makedirs(folderPath, exist_ok=True)
    
    commonAdFilePath = os.path.join(folderPath, "common_ad_names.txt")

    if not os.path.exists(commonAdFilePath):
        with open(commonAdFilePath, "w") as file:
            file.write("Advertisement\n")
            file.write("LISTEN NOW\n")
            file.write("—\n")
            file.write("Listen to music, ad-free.\n")

    with open(commonAdFilePath, "r") as commonAdNamesFile:
        for line in commonAdNamesFile:
            commonAdNames.append(line.strip())

    while running:
        audioTitle = await getSongTitle()
        if audioTitle in commonAdNames:
            await restartSpotify()
            await asyncio.sleep(60) # Impossible to have an ad immediately after reopening the app
        elif audioTitle.startswith("ERROR"):
            print("Error fetching Spotify song title")
            await asyncio.sleep(30) # Saves resources because Spotify is probably not running
        else:
            print("Song detected")

        await asyncio.sleep(2)

def startProgram():
    asyncio.run(program())

def onQuit(icon):
    global running
    running = False
    icon.stop()

if __name__ == "__main__":
    mutex = win32event.CreateMutex(None, False, "SpotifyAdAvoiderMutex")

    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS: # Closes new instance of program if one is already running
        sys.exit(0)

    programPath = sys.executable

    threading.Thread(target=startProgram, daemon=True).start()

    icon = createTrayIcon(onQuit, programPath)
    icon.run()