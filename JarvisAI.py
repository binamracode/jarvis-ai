import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

voiceRate = 180
engine.setProperty('rate', voiceRate)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time():
	time = datetime.datetime.now().strtime('%I : %M : %S')


def date():
    year = int( datetime.datetime.now().year )
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)


hour = datetime.datetime.now().hour


if hour >= 5 and hour < 12:
    speak('Good morning ')
elif hour >= 12 and hour < 17:
    speak('Good afternoon ')
elif hour >= 17 and hour < 19:
    speak ('Good evening ')

else :
    speak ('Good night ')
    
    


def wishme():
    
    speak('welcome back sir')

    speak('jarvis at your service..')
    speak('what can i do for you?')


wishme()