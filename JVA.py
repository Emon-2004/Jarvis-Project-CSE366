import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# def processCommand(c):
#     pass

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

                    # processCommand()

        except Exception as e:  #Just In case google speech api or internet is down
            print("Google Speech Recognition could not understand audio; {0}".format(e))