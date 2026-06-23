import time

from spotify import restartSpotify, getSongTitle

running = True

def program():
    while running:
        audioTitle = getSongTitle()
        if audioTitle == "Advertisement" or audioTitle == "LISTEN" or audioTitle == "test":
            restartSpotify()
            time.sleep(60)
        else:
            if audioTitle.startswith("ERROR"):
                print("Error fetching Spotify song title.")
                time.sleep(10) # Saves resources because Spotify is probably not running

        time.sleep(1)

program()