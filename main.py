import asyncio

from spotify import restartSpotify, getSongTitle

running = True

async def program():
    while running:
        audioTitle = await getSongTitle()
        if audioTitle == "Advertisement" or audioTitle == "LISTEN NOW":
            restartSpotify()
            await asyncio.sleep(60) # Impossible to have an ad immediately after reopening the app
        elif audioTitle.startswith("ERROR"):
            print("Error fetching Spotify song title")
            await asyncio.sleep(10) # Saves resources because Spotify is probably not running
        else:
            print("Song detected")

        await asyncio.sleep(1)

asyncio.run(program())