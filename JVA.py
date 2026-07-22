import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open stackoverflow" in c.lower():
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
    elif "open gmail" in c.lower():
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        print("Recognizing...")
        # recognize speech using Google Speech Recognition
        try:
            with  sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit = 3)      
            word = r.recognize_google(audio)
            print(f"Heard: {word}")
            if("jarvis" in word.lower()):
                speak("Ya")
                # Listen for command
                with  sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)      
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:  #Just In case google speech api or internet is down
            print("Google Speech Recognition could not understand audio; {0}".format(e))