import speech_recognition as sr
import os
import pyautogui

def ui_ConfirmMsg(Desc, Ttl):
    if pyautogui.confirm(text=Desc, title=Ttl) == "OK":
        return "OK"
    else:
        return "CANCEL"

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
    
    query = query.lower()

    if query == "close program":
        if ui_ConfirmMsg('Are you sure you want to close the program?', 'Are you sure?') == "OK":
            quit()
        else:
            print("CANCELLED - close program")
            
    if query == "lock system":
        if ui_ConfirmMsg('Are you sure you want to lock your system?', 'Are you sure?') == "OK":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        else:
            print("CANCELLED - lock system")
            
    if query == "shutdown" or query == "shut down":
        if ui_ConfirmMsg('Are you sure you want to shutdown your system?', 'Are you sure?') == "OK":
            os.system("shutdown /s /t 1")
        else:
            print("CANCELLED - shutdown/shut down")

while True:
    speech_recognition()
