import os
import subprocess
import winrt.windows.media.control
import asyncio

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

async def restartSpotify():
    subprocess.run(["taskkill", "/f", "/im", "Spotify.exe"], creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True)

    await asyncio.sleep(1)

    appData = os.getenv("APPDATA", "")
    pathName = os.path.join(appData, "Spotify", "Spotify.exe")

    if os.path.exists(pathName):
        os.startfile(pathName) # For website downloaded version
    else:
        os.startfile("spotify:") # For Microsoft Store version

    await asyncio.sleep(5)

    manager = await winrt.windows.media.control.GlobalSystemMediaTransportControlsSessionManager.request_async()
    session = manager.get_current_session()

    if session:
        await session.try_play_async()
    else:
        print("ERROR - Failed to resume audio playback")