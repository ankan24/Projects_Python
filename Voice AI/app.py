import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    playsound.playsound("temp.mp3")

    speak("Hello, world!")
    
    os.remove("temp.mp3")