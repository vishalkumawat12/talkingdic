from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import requests
import time


def audio(txt):

    var1 = gTTS(txt, lang='en')
    var1.save('hello.mp3')
    playsound("hello.mp3")
    os.remove('hello.mp3')


def query():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print(audio)

        try:
            print("converting")
            query = r.recognize_google(audio, language='en-us')
            print(query)
            return query

        except Exception as e:
            print(e)


if __name__ == "__main__":
    txt="welcome to our library. \n this is a talking library"
    audio(txt)
    while True:
        Query=query()
        print(Query)
        meaning = requests.get(
            'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+Query)
        # print(meaning.json())

        # os.system("cls")
        pronoun = meaning.json()
        aud=str(pronoun[0]['phonetics'][0]['audio'])
        audio("the pronounciation of this word is")
        playsound(aud)
        os.system("cls")
        txt = pronoun[0]['meanings'][0]['definitions'][0]['definition']
        audio(txt)
        time.sleep(5)
        audio("do you want to search again , then say yes or if not then say anything")
        againSrearch=query()
        if againSrearch=='no':
            break