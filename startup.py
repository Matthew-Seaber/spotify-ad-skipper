import os
import winshell
from win32com.client import Dispatch

def getStartupPath():
    return os.path.join(winshell.startup(), "Spotify Ad Avoider.lnk")

def checkStartupEnabled():
    return os.path.exists(getStartupPath())

def enableStartup(programPath):
    shortcutPath = getStartupPath()

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcutPath)
    shortcut.Targetpath = programPath
    shortcut.WorkingDirectory = os.path.dirname(programPath)
    shortcut.save()

def disableStartup():
    shortcutPath = getStartupPath()

    if os.path.exists(shortcutPath):
        os.remove(shortcutPath)