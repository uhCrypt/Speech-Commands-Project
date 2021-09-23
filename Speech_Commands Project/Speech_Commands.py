import subprocess
import speech_recognition as sr
import os

def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        audio = r.listen(source)
    print(audio)
    
    try:
        r.pause_threshold = 1
        r.energy_threshold = 4000
        query = r.recognize_google(audio)
        
    except sr.UnknownValueError as e:
        print(f"speech_recognition.UnknownValueError: {e}")
        query = ""
    except sr.RequestError as e:
        print(f"speech_recognition.RequestError: {e}")
        query = ""
    except Exception as e:
        print(f"Other exception: {e}")
        query = ""

    print(query)

    if "lock" in query: # all of these being "if" makes it so you can string them together, so you can, for exmaple, say "lock and quit"
        os.system("rundll32.exe user32.dll,LockWorkStation")
    if "shutdown" in query or "shut down" in query:
        os.system("shutdown /s /t 1")
    if "open steam" in query:
        subprocess.check_call([r"C:\Program Files (x86)\Steam\Steam.exe"])

speech_recognition()
