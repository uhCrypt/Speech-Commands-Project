import subprocess
import speech_recognition as sr
import os
import json
import keyboard
from winsound import Beep

def fetch_commands() -> dict:
    """
    :return: dictionary "commands.json"
    """
    with open("commands.json", "r") as fh:
        return json.load(fh)

def speech_recognition():
    with open(".//Data//Settings.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    print("Press", jsonObject["activateKey"], "to speak.")
    while True:
      if keyboard.is_pressed(jsonObject["activateKey"]): # of course, you should add more here to create a good combo
            r = sr.Recognizer()
            with sr.Microphone() as source:
                with open(".//Data//Settings.json") as jsonFile:
                    jsonObject = json.load(jsonFile)
                    jsonFile.close()
                    
                if jsonObject["beepSounds"] == "True":
                    # "listening" beep
                    Beep(523, 50)
                    Beep(784, 150)
                print("Awaiting voice input...")
                
                if jsonObject["waitForAudioInput"] == "True":
                    audio = r.listen(source)
                else:
                    audio = r.listen(source, phrase_time_limit=jsonObject["waitForAudioTimer"])
            
            print("Analysing audio...\n")
            if jsonObject["beepSounds"] == "True":
                Beep(784, 50)
                Beep(1047, 150)
    
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

            print(f"'{query}'")

            query = query.lower()

            command_phrase = "hey computer"
            command_phraseBACKUP = "a computer"
            if not query.startswith(command_phrase) or not query.startswith(command_phraseBACKUP): return False

            global commands
            commands = fetch_commands()

            for key in commands.keys():
                if key.lower() in query:
                    exec(commands[key])
                    
        
while True:
    speech_recognition()
