# Modules
import subprocess
import sys
import platform
import time
import zipfile
import os

print(sys.argv[0])

# Functions
def install(package):
    #subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    os.system('python -m pip install ' + os.path.join(package))

# Unzipping files
with zipfile.ZipFile(os.path.join(".\\Packages\Zipped\PyAudio.zip"), 'r') as zip_ref:
    zip_ref.extractall(os.path.join(".\\Packages\\Unzipped"))

print("Checking platform bit...")
platform_Version = platform.architecture()[0]

if platform_Version == "32bit" or platform_Version == "64bit":
    print(platform_Version, "platform detected.\nChecking python version...")
    
    python_Version_Normal = platform.python_version()
    python_Version_Tuple = platform.python_version_tuple()
    python_Version_Digit = python_Version_Tuple[0] + "" + python_Version_Tuple[1]
    
    print("Python", python_Version_Normal, "detected.\nChecking for a compatable PyAudio module...")
    
    if int(python_Version_Digit) >= 27 and int(python_Version_Digit) <= 39:
        print("Compatable PyAudio module found.\nAttempting to download and install PyAudio...")

        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        if 'PyAudio' in installed_packages:
            print("PyAudio is already installed, skipping step.")
        else:
            if platform_Version == "64bit":
                if int(python_Version_Digit) >= 38:
                    install(".\\Packages\\Unzipped\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "-win_amd64.whl")
                else:
                    install(".\\Packages\\Unzipped\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "m-win_amd64.whl")
            else:
                if int(python_Version_Digit) >= 38:
                    install(".\\Packages\\Unzipped\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "-win32.whl")
                else:
                    install(".\\Packages\\Unzipped\\PyAudio\\PyAudio-0.2.11-cp" + python_Version_Digit + "-cp" + python_Version_Digit + "m-win32.whl")
            print("Successfully installed PyAudio.")

        print("Attempting to download and install SpeechRecognition...")
        
        if 'SpeechRecognition' in installed_packages:
            print("SpeechRecognition is already installed, skipping step.")
        else:
            install("SpeechRecognition")
            print("Successfully installed SpeechRecognition.")

        print("Setup complete - This program will automatically terminate.")
        time.sleep(3)
        os.remove()
    else:
        print("You don't have a compatable Python Version installed. Please make sure you have Python 2.7.0 - Python 3.9.9 installed.")
else:
    print("32bit or 64bit platform not detected. Please manually install the packages required in the 'Setup_Log.txt' file.")
    sys.exit()
