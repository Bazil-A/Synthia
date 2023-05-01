from gtts import gTTS
from playsound import playsound
import time

language = 'en'


def speak(sentence):
    tts = gTTS(text = sentence, lang = language)
    tts.save('speech.mp3')
    playsound('speech.mp3')

speak("Hello world")
speak("My name is Synthia")
