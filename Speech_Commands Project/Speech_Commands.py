import subprocess
import speech_recognition as sr
import os
import webbrowser
import pyautogui
import time

def ui_ConfirmMsg(Desc, Ttl):
    if pyautogui.confirm(text=Desc, title=Ttl) == "OK":
        return "OK"
    else:
        return "CANCEL"

def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Awaiting voice input...")
        audio = r.listen(source, phrase_time_limit=5)
            
    print(audio)
    
    try:
        r.pause_threshold = 1
        r.energy_threshold = 4000
        query = r.recognize_google(audio, language="en-GB")
        
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

    query = query.lower()

    command_phrase = "hey computer"
    if not query.startswith(command_phrase): return False

    # if query == "exit program":
    if "exit program" in query:
        if ui_ConfirmMsg('Are you sure you want to exit the program?', 'Are you sure?') == "OK":
            quit()
        else:
            print("CANCELLED - exit program")
            
    if "lock system" in query:
        if ui_ConfirmMsg('Are you sure you want to lock your system?', 'Are you sure?') == "OK":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        else:
            print("CANCELLED - lock system")
            
    if query == "shutdown" or query == "shut down":
        if ui_ConfirmMsg('Are you sure you want to shutdown your system?', 'Are you sure?') == "OK":
            os.system("shutdown -s -t 0")
        else:
            print("CANCELLED - shutdown/shut down")
            
            
    if query == "open steam":
        subprocess.check_call([r"C:\Program Files (x86)\Steam\Steam.exe"])
        
    if query == "open opera":
        subprocess.check_call([r"C:\Users\uhcry_8hxodbw\AppData\Local\Programs\Opera GX\launcher.exe"])
        
while True:
    speech_recognition()
