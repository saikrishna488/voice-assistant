import speech_recognition as sr
from time import ctime
import webbrowser
import time
from gtts import gTTS
import os
from playsound import playsound
import random

r = sr.Recognizer()

def recordAudio(ask=False):
    with sr.Microphone() as source:
        if ask:
            pyTalk(ask)
        audio = r.listen(source,timeout=5, phrase_time_limit=5)
        try:
            voice_data = r.recognize_google(audio)
            pyTalk("You said: " + voice_data)
            return voice_data
        except sr.UnknownValueError:
            pyTalk("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError:
            pyTalk("Sorry, my speech service is down.")
            return ""

def respond(voice_data):
    if 'what is your name' in voice_data:
        pyTalk("My name is pyAssith")
    if 'what time is it' in voice_data:
        pyTalk("It's " + str(ctime()))
    if 'search' in voice_data:
        search = recordAudio("What do you want to search?")
        if len(search) > 1:
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            pyTalk("Here is what I found for: " + search)
        else:
            pyTalk("I didn't understand your search query.")
    if 'find location' in voice_data:
        pyTalk("What is the location?")
        location = recordAudio()  # Listen for location without a prompt
        if len(location)>1:
            url = 'https://www.google.com/maps/search/' + location
            webbrowser.get().open(url)
            pyTalk("Here is the location of " + location)
        else:
            pyTalk("I didn't understand the location query.")
    if 'exit' in voice_data:
        pyTalk("Goodbye!")
        exit()

def pyTalk(audio):
    tts = gTTS(text=audio,lang='en')
    r = random.randint(1,1000000)
    audio_file = "audio-"+str(r)+".mp3"
    tts.save(audio_file)
    playsound(audio_file)
    print(audio)
    os.remove(audio_file)

pyTalk("How can I help you?")
while True:
    voice_data = recordAudio()
    if voice_data:
        respond(voice_data)
