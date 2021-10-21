# Modules
import subprocess
import sys
import platform
import time
import zipfile
import os


# Setup Confirmation
userInput = input("""Are you sure you want to run the automatic uninstall?
It WILL uninstall the following packages:

PyAudio - v0.2.11
----------------------------------
SpeechRecognition - v3.8.1
----------------------------------
PyAutoGUI - v0.9.53
----------------------------------
Keyboard - v0.13.5

Y/N
""")

if userInput.lower() == "y":
    print("Starting automatic uninstall...\n")
    time.sleep(2.5)
else:
    print("Automatic uninstall cancelled. Exiting...")
    time.sleep(2.5)
    quit()

# Functions
def uninstallPath(packageInfo):
    print(f"\nUninstalling {packageInfo}...\n")
    os.system(f"python -m pip uninstall {os.path.join(packageInfo)}")
    print(f"\nUninstalled {packageInfo}.\n")

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

if 'PyAudio' in installed_packages:
    uninstallPath("PyAudio")
else:
    print("\nPyAudio wasn't installed on your system. Skipping...\n")

if 'SpeechRecognition' in installed_packages:
    uninstallPath("SpeechRecognition")
else:
    print("\nSpeechRecognition wasn't installed on your system. Skipping...\n")

if 'PyAutoGUI' in installed_packages:
    uninstallPath("pyautogui")
else:
    print("\nPyAutoGui wasn't installed on your system. Skipping...\n")

if 'keyboard' in installed_packages:
    uninstallPath("keyboard")
else:
    print("\Keyboard wasn't installed on your system. Skipping...\n")

print("\nUninstallation complete - This program will automatically terminate.\n")
time.sleep(5)
quit()
