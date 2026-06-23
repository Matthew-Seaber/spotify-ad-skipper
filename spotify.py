import os
import time
import subprocess

def getSongTitle():
    try:
        return "test"
    except:
        return "ERROR - Spotify may not be running"

def restartSpotify():
    os.system("taskkill /f /im Spotify.exe")

    time.sleep(1)

    appData = os.getenv("APPDATA", "")
    pathName = os.path.join(appData, "Spotify", "Spotify.exe")

    if os.path.exists(pathName):
        subprocess.Popen(pathName) # For website downloaded version
    else:
        os.system("start spotify:") # For Microsoft Store version