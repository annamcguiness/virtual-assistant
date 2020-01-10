import speech_recognition as sr
import scrape

import tts

name = ''
listening = False

r = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic as source:
        print('Say something!')
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        said = r.recognize_google(audio)
        # Recognize google audio is currently being ran with default google key
        # If used in production, change api key to non default one.
        print("Google Speech Recognition thinks you said " + said)
    except sr.UnknownValueError:
        tts.play("I don't understand. Could you repeat that?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if "hey Alex" in said:
        tts.play('Yes?')
        listening = True

    if listening:
        if said == "what is your goal" or said == "what's your goal":
            tts.play('World domination ha ha ha')
            listening = False
        if said.startswith("call me"):
            name = said.replace("call me", '')
            tts.play("Hello, " + name)
            listening = False
        if said == "what is my name" or said == "what's my name":
            if name == '':
                tts.play("You have not told me your name")
            else:
                tts.play("Your name is " + name)
                listening = False
        if said.startswith("what is"):
            srch = said.replace("what is", '')
            ans = scrape.search(srch)
            tts.play(ans)
        if said.startswith("what's"):
            srch = said.replace("what's", '')
            ans = scrape.search(srch)
            tts.play(ans)
        if said.startswith("who is"):
            srch = said.replace("who is", '')
            ans = scrape.search(srch)
            tts.play(ans)
        if said.startswith("who's"):
            srch = said.replace("who's", '')
            ans = scrape.search(srch)
            tts.play(ans)



