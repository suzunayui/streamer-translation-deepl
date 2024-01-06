import os
from dotenv import load_dotenv
import deepl
import speech_recognition as sr

load_dotenv()
translator = deepl.Translator(os.getenv("deepl_api_key"))
listener = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source, phrase_time_limit=4)
            voice_text = listener.recognize_google(voice, language="ja-JP")
            print(voice_text)
            result = translator.translate_text(voice_text, target_lang="EN-US")
            print(result)
            print()
    except:
        pass