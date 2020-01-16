import os

import tts


def open(inp):
    dir = os.getcwd()
    dir = dir+"\shortcuts"
    print("Opening file from: "+dir)
    inp.title()
    try:
        os.startfile(dir+"\\"+inp+".lnk")
    except:
        tts.play("Shortcut not found")