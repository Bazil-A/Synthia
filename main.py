from gtts import gTTS
from playsound import playsound
from datetime import datetime

language = 'en'

# Speaks the input string via TTS
def speak(sentence):
    tts = gTTS(text = sentence, lang = language)
    tts.save('speech.mp3')
    playsound('speech.mp3')

# For initializations and startup speech
def startup():
    speak("Hello World! My name is Synthia!")

# Retrieves the current time 
def getTime():
    currentTime = datetime.now().strftime("%I:%M %p")
    speak("The current time is " + currentTime)

# Main function
def main():
    startup()

#Call main function 
main()
