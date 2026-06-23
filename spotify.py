import os
import time
import subprocess
import asyncio
import winrt.windows.media.control

async def getSongTitle():
    try:
        manager = await winrt.windows.media.control.GlobalSystemMediaTransportControlsSessionManager.request_async()
        session = manager.get_current_session()
        sessionProperties = await session.try_get_media_properties_async()
        
        if session is None or sessionProperties is None:
            return "ERROR - Spotify is not running"
    
        print(sessionProperties.title)
        return sessionProperties.title
    except Exception as e:
        print("Error:", e)
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