import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listner=sr.Recognizer()
engine=pyttsx3.init()

voices = engine.getProperty('voices')

if len(voices)>1:
    engine.setProperty('voice',voices[1].id)
    
else:
    engine.setProperty('voice',voices[0].id)
    
def engine_talk(text):
    print(f"Alexa is saying: {text}")
    engine.say(text)
    engine.runAndWait()
    
def user_command():
    try:
        with sr.Microphone() as source:
            listner.adjust_for_ambient_noise(source)
            print("Start speaking..!")
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            
            if 'alexa' in command:
                command=command.replace('alexa',"")
                print(f"User said: {command}")
                return command
    except Exception as e:       
        print(f"Error: {e}")
    return ""
def run_alexa():
    command=user_command()
    if command:
        if 'play' in command:
            song=command.replace('play','')
            engine_talk('Playing'+song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time=datetime.datetime.now().strftime('%I:%M:%p')
            engine_talk("The Current time is " + time)
        elif 'who is' in command:
            name=command.replace('who is',"")
            info=wikipedia.summary(name,1)
            print(info)
            engine_talk(info)
        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())
        elif 'stop' in command:
            sys.exit()
        else:
            engine_talk("i could not hear you properly")
    else:
        engine_talk("i did not catch that.Please speak again")
        
while True:
    run_alexa()
            
            
            
            