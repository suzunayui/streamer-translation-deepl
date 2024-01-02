import speech_recognition as sr
import os
from dotenv import load_dotenv

listener = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice, language="ja-JP")
            print(voice_text)
    except:
        print('Sorry, I could not listen')