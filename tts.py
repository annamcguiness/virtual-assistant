from gtts import gTTS
import os
from playsound import playsound


def play(t):
    tts = gTTS(text=t, lang='en')
    tts.save("good.mp3")
    playsound('good.mp3')
    os.remove("good.mp3")
