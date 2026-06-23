import os
import time
import subprocess
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

async def getSongTitle():
    try:
        mediaSession = await MediaManager.request_async().get_current_session()

        if mediaSession is None:
            return "ERROR - Spotify is not running"
        
        mediaDetails = await mediaSession.try_get_media_properties_async()#
        title = mediaDetails.title

        if mediaDetails is None or title is None:
            return "ERROR - Problem fetching current audio details"

        return title
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