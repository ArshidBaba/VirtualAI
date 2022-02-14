import speech_recognition as sr
import pyttsx3
import pywhatkit
listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():    
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listner.listen(source)
            print("passed")
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'jack' in command:
                command = command.replace("jack", '')
                print(command)
    except:
        pass
    return command

def run_feinman():
    # engine.say("Hello Arshid")
    # engine.say('What can I do for you sir?')
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


run_feinman()