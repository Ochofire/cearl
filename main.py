from tkinter.constants import NUMERIC, X
import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser

from wikipedia.wikipedia import search

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'thank you' in command:
        talk('Your Welcome')
    elif 'what is ' in command:
        ob = command.replace('what is ', '')
        info = wikipedia.summary(ob, 3)
        print(info)
        talk(info)

    elif 'today' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'well done' in command:
        talk('Thank You')


    elif 'your name' in command:

        talk('Python')

    elif 'open chrome' in command:
        subprocess.call("C:/Program Files/Google/Chrome/Application/chrome.exe")
        talk("Opening Chrome")

    elif 'open code' in command:
        talk("Opening Visual Studio Code")
        subprocess.call("C:/Users/Andrew Onyilokwu/AppData/Local/Programs/Microsoft VS Code/code.exe")
        talk('Done')
    elif 'search for' in command:
        ob = command.replace('search for ', '')
        talk('searching For' + ob)
        pywhatkit.search(ob)






    elif 'python' in command:
        talk("Hi Emmanuel")


    elif 'calculate' in command:
        num1 = input("Number:")
        num2 = input("Number:")
        post = int(num1) + int(num2)
        print(post)
        talk(post)
    elif ' decimal' in command:
        num1 = input("Number:")
        num2 = input("Number")
        post = float(num1) + float(num2)
        print(post)
        talk(post)

    elif 'bye' in command:
        talk("Bye, See You Later")
        exit(run_alexa)



    elif 'open charm' in command:
        subprocess.call("C:/Program Files/JetBrains/PyCharm Community Edition 2021.2.1/bin/pycharm64.exe")
        talk("Opening Py Charm")


    elif 'read' in command:
        import pyttsx3
        from tkinter import filedialog

        filename = filedialog.askopenfilename()
        file = open(filename, 'r')

        text = file.read()

        text

        play = pyttsx3.init()
        print(text)

        voices = play.getProperty('voices')
        play.setProperty('voice', voices[1].id)

        play.say(text)
        play.runAndWait()

        file.close()
    elif 'how are you' in command:
        talk('I Am Fine Thank You')

    elif 'who made you' in command:
        talk('EMMANUEL ANDREW')

    elif 'do you work for the cia' in command:
        talk(' of course not')

    elif 'multiply' in command:
        num1 = input('Number:')
        num2 = input("Number:")
        sult = int(num1) * int(num2)
        print(sult)
        talk(sult)
    elif 'divide' in command:
        num1 = input('Number:')
        num2 = input("Number:")
        sult = int(num1) / int(num2)
        print(sult)
        talk(sult)
    elif 'subtract' in command:
        num1 = input('Number:')
        num2 = input("Number:")
        sult = int(num1) - int(num2)
        print(sult)
        talk(sult)
 
     





















    elif 'hi' in command:
        talk('Hello Emmanuel')



    else:
        talk('Sorry I Did Not Get You')


while True:
    run_alexa()