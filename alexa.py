import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os 

engine= pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak up you Son of a bitch")
        r.pause_threshold=1
        audio=r.listen(source)
    
    
    try:
        print("Hold lemme think")
        query=r.recognize_google(audio, language='en-in')
        print("User said" + query + "\n ")
    except Exception as e:
        print(e)
        speak("BRO you are so dumb you werent able to make me understand")
        return "None"
    return query
if __name__== "__main__":
    speak("Your real dad is activated")
    speak("tell me what help does your dumbass needs now")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'creator' in query:
            speak("I am your dad developed by Lord Tejas")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
       
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            exit(0)
    