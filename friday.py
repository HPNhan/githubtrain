import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import pyaudio

friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print('F.R.I.D.A.Y.:' + audio)
    friday.say(audio)
    friday.runAndWait()   

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning Nhan ")  
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Nhan ")
    elif hour >= 18 and hour < 24:
        speak("Good night Nhan ")
    speak("how can i help you")    

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 1
        audio = c.listen(source)
    try:
        query = c.recognize_sphinx(audio, language='en')
        print("TONY: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")    
        query = str(input('Your oder is: '))
    return query    

if __name__ == "__main__":
    welcome()    
    while True:
        query = command().lower()
        if "google" in query:
            speak("what should i search boss? ")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube" in query:
            speak("what should i search boss? ")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')    