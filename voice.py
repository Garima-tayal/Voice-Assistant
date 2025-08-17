import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

engine = pyttsx3.init()
engine.setProperty("rate", 170)   
engine.setProperty("volume", 1)  

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("🔎 Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, I didn't get that. Please say again.")
        return "None"

def main():
    speak("Hello Garima, I am your voice assistant.")
    while True:
        query = listen()

        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "play music" in query:
            music_dir = "C:/Users/Welcome/Music"  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "stop" in query or "exit" in query or "quit" in query:
            speak("Goodbye, have a great day!")
            break

if __name__ == "__main__":
    main()
