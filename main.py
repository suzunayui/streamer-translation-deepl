import speech_recognition as sr
import os
from dotenv import load_dotenv
import deepl

load_dotenv()
deepl_api_key = os.environ['deepl_api_key']
listener = sr.Recognizer()

ja_name = "すずなゆい"
en_name = "suzuna yui"

translator = deepl.Translator(deepl_api_key)

while True:
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice, language="ja-JP")
            result_text = translator.translate_text(voice_text, target_lang="EN-US")
            print(ja_name + ":" + voice_text)
            print(en_name + ":" + str(result_text))
            print()
    except:
        pass