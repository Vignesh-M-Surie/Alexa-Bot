import speech_recognition as sr
import pyttsx3
import pywhatkit
import  datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

l = []
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Hi i am alexa, what can i do for you today?')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command= command.replace('shashi','')

    except:
        pass
    return command

def run_shashi():
    global l
    global a
    command= take_command()
    if 'play' in command:
        command= command.replace('play','')
        talk('playing'+ command)
        print('playing'+ command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
    elif 'what is' in command:
        command=command.replace("what is",'')
        info=wikipedia.summary(command,1)
        talk('searching for' + command)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk("Okay untill we meet next time")
        a=0
        return a
    else:
        l.append(command)
        talk("Sorry i didnt get you, can you repeat again?")
global a
a=1
while a==True:
    run_shashi()
