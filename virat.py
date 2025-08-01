import speech_recognition as sr
import requests
import webbrowser
import pyttsx3
import musiclibrary
import wikipedia
from datetime import datetime
import os
import subprocess
from config import API_KEY


recognizer = sr.Recognizer()


def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            speak(f"Sorry, I couldn't find the weather for {city}.")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}.")
    
    except Exception as e:
        speak("Something went wrong while fetching the weather.")
    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open stack overflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
        speak("Opening Stack Overflow.")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
        speak("Opening GitHub.")

    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT.")

    elif "open google maps" in c.lower():
        webbrowser.open("https://www.google.com/maps")
        speak("Opening Google Maps.")

    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp.")

    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail.")

    elif "open youtube music" in c.lower():
        webbrowser.open("https://music.youtube.com")
        speak("Opening YouTube Music.")

    elif "time" in c.lower():
        now= datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")

    elif "date" in c.lower():
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}.")

    elif "shutdown" in c.lower():
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    elif "restart" in c.lower():
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")

    elif "lock" in c.lower():
        speak("Locking the system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "open notepad" in c.lower():
        speak("Opening Notepad.")
        subprocess.Popen(["notepad.exe"])

    elif "open calculator" in c.lower():
        speak("Opening Calculator.")
        subprocess.Popen("calc.exe")

    elif "open code" in c.lower():
        speak("Opening Visual Studio Code.")
        os.system("code")

    elif "weather" in c.lower():
        speak("Which city's weather do you want?")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for city...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            city = recognizer.recognize_google(audio)
            print(f"City: {city}")
            get_weather(city)

    elif "search" in c.lower():
        query = c.lower().replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query} on Google.")
        else:
            speak("Please specify what you want to search for.")

    elif "who is" in c.lower() or "what is" in c.lower():
        topic = c.lower().replace("who is", "").replace("what is", "").strip()
        summary= wikipedia.summary(topic, sentences=2)
        speak(f"According to Wikipedia, {summary}")

    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip() # Remove 'play' if present
        song = song.replace("song", "").strip()  # Remove 'song' if present
        if song in musiclibrary.music.values():
            for url, title in musiclibrary.music.items():
                if title == song:
                    webbrowser.open(url)
                    speak(f"Playing {title} on YouTube.")
                    break
        else:
            speak("Sorry, I couldn't find that song in my library.")

    elif "exit" in c.lower() or "quit" in c.lower():
        speak("Thankyou and Have a great day.")
        exit()

    else:
        pass


# After running code it speaks this
if __name__=="__main__":
    speak("Initializing the voice assistant Virat. Please wait...")

    try:
        while True:
       
            try:
             # Listens from microphone
             with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=8)
                word = recognizer.recognize_google(audio)

             #listens for the keyword "virat"
                print(f"You said: {word}")
                if(word.lower() == "hello virat" or word.lower() == "hi virat" or word.lower() == "hey virat" or word.lower() == "virat" or word.lower() == "hello"):
                    speak("Yes, how can I assist you?")
                

                 #if keyword is detected, listens for the next command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        print("Virat is listening...")
                        audio = recognizer.listen(source,timeout=5,phrase_time_limit=8)
                        command = recognizer.recognize_google(audio)
                        print(f"Command received: {command}")

                        processCommand(command)

            except sr.UnknownValueError:
                speak("Sorry, I did not catch that. Could you please repeat?")
            except sr.RequestError as e:
                speak(f"Could not request results; {e}")
            except sr.WaitTimeoutError:
                print("Listening timed out, please try again.")
    except KeyboardInterrupt:
        print("\nVoice assistant terminated by user.")
        speak("Thank you for using the voice assistant Virat. Goodbye")