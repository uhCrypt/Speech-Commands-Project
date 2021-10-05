# Modules
import subprocess
import sys
import platform
import time
import zipfile
import os


# Setup Confirmation
userInput = input("""Are you sure you want to run the automatic setup?
It WILL install the following packages (in order of installation):

PyAudio - v0.2.11
----------------------------------
SpeechRecognition - v3.8.1
----------------------------------
PyAutoGUI - v0.9.53

Y/N
""")

if userInput.lower() == "y":
    print("Starting automatic setup...")
    time.sleep(2.5)
else:
    print("Automatic setup cancelled. Exiting...")
    time.sleep(2.5)
    quit()


# Functions
def installPath(packageInfo):
    os.system('python -m pip install ' + os.path.join(packageInfo))

def installModule(packageName, packageInfo):
    print("Attempting to download and install", packageName + "...\n")
    subprocess.check_call([sys.executable, "-m", "pip", "install", packageInfo])
    print("Successfully installed ", packageName + ".\n")

print("Checking platform bit...\n")
platform_Version = platform.architecture()[0]


# Main code - Checks platform bit, checks Python version, checks if modules are installed - if not installs them.
if platform_Version == "32bit" or platform_Version == "64bit":
    print(platform_Version, "platform detected.\n\nChecking python version...\n")
    
    python_Version_Normal = platform.python_version()
    python_Version_Tuple = platform.python_version_tuple()
    python_Version_Digit = python_Version_Tuple[0] + "" + python_Version_Tuple[1]
    
    print("Python", python_Version_Normal, "detected.\n\nChecking for a compatible PyAudio module...\n")
    
    if int(python_Version_Digit) >= 34 and int(python_Version_Digit) <= 39:
        print("Compatible PyAudio module found.\n\nAttempting to download and install PyAudio...\n")

        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        # Installing PyAudio
        if 'PyAudio' in installed_packages:
            print("PyAudio is already installed, skipping step.\n")
        else:
            # Unzipping files
            with zipfile.ZipFile(os.path.join(".\\Packages\\PyAudio_Compressed.zip"), 'r') as zip_ref:
                zip_ref.extractall(os.path.join(".\\Packages"))
            # Running installation
            if platform_Version == "64bit":
                if int(python_Version_Digit) >= 38:
                    installPath(".\\Packages\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "-win_amd64.whl")
                else:
                    installPath(".\\Packages\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "m-win_amd64.whl")
            else:
                if int(python_Version_Digit) >= 38:
                    installPath(".\\Packages\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "-win32.whl")
                else:
                    installPath(".\\Packages\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "m-win32.whl")
            print("Successfully installed PyAudio.\n")
        
        # Installing SpeechRecognition
        if 'SpeechRecognition' in installed_packages:
            import speech_recognition as sr
            if sr.__version__ == "3.8.1":
                print("SpeechRecognition is already installed, skipping step.\n")
            else:
                userInput = input("SpeechRecognition is installed but the wrong version is installed. Would you like to install the recommended version?\n\nY/N\n")
                if userInput.lower() == "y":
                    installModule("SpeechRecognition", "SpeechRecognition==3.8.1")
                else:
                    print("Skipping SpeechRecognition installation of recommended version.\n")

        else:
            installModule("SpeechRecognition", "SpeechRecognition==3.8.1")
            print("Successfully installed SpeechRecognition.\n")

        # Installing PyAutoGUI
        if 'PyAutoGUI' in installed_packages:
            import pyautogui as pyg
            if pyg.__version__ == "0.9.53":
                print("PyAutoGui is already installed, skipping step.\n")
            else:
                userInput = input("PyAutoGui is installed but the wrong version is installed. Would you like to install the recommended version?\n\nY/N\n")
                if userInput.lower() == "y":
                    installModule("PyAutoGui", "pyautogui==0.9.53")
                else:
                    print("Skipping PyAutoGui installation of recommended version.\n")
        else:
            installModule("PyAutoGui", "pyautogui==0.9.53")
            print("Successfully installed PyAutoGui.\n")

        #print("Clearing files...")
        #os.remove(os.path.join(".\\Packages\\PyAudio"))

        print("Setup complete - This program will automatically terminate.\n")
        time.sleep(5)
        quit()
    else:
        print("You don't have a compatible Python Version installed. Please make sure you have Python 3.4.X - Python 3.10.X installed.")
        time.sleep(5)
        quit()
else:
    print("32bit or 64bit platform not detected. Please manually install the packages required in the 'Manual.txt' file.")
    time.sleep(5)
    quit()
