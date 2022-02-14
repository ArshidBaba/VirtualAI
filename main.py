import speech_recognition as sr

listner = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listner.listen(source)
        print("passed")
        command = listner.recognize_google(voice)
        command = command.lower()
        if 'feinman' in command:
            print(command)
except:
    pass