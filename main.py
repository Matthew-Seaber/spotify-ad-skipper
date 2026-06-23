import asyncio
import threading
import sys
import os

from spotify import restartSpotify, getSongTitle
from tray import createTrayIcon

running = True
commonAdNames = []

async def program():
    commonAdFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "common_ad_names.txt")
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
    programPath = sys.executable

    threading.Thread(target=startProgram, daemon=True).start()

    icon = createTrayIcon(onQuit, programPath)
    icon.run()