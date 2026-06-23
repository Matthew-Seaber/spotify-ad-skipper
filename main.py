import asyncio
import threading

from spotify import restartSpotify, getSongTitle
from tray import createTrayIcon

running = True

async def program():
    while running:
        audioTitle = await getSongTitle()
        if audioTitle == "Advertisement" or audioTitle == "LISTEN NOW" or audioTitle == "—" or audioTitle == "Listen to music, ad-free." or audioTitle == "Lighter":
            await restartSpotify()
            await asyncio.sleep(60) # Impossible to have an ad immediately after reopening the app
        elif audioTitle.startswith("ERROR"):
            print("Error fetching Spotify song title")
            await asyncio.sleep(10) # Saves resources because Spotify is probably not running
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
    threading.Thread(target=startProgram, daemon=True).start()

    icon = createTrayIcon(onQuit)
    icon.run()