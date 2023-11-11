# Net_Switch was created by Speed3DBall

import subprocess
import time

global result

def ethernet_check():
    global result
    result = subprocess.run(['netsh', 'interface', 'show', 'interface', 'Ethernet'], capture_output=True, text=True)

def disable_ethernet():
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'Ethernet', 'admin=disable'])
    ethernet_check()
    if not 'Disabled' in result.stdout:
        crash()
    else:
        print("Disabling Ethernet connection.............")
        print("------------------------------------------")
        print("Net_Switch script was made by Speed3DBall.")
        time.sleep(2)

def enable_ethernet():
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'Ethernet', 'admin=enable'])
    ethernet_check()
    if not 'Enabled' in result.stdout:
        crash()
    else:
        print("Enabling Ethernet connection..............")
        print("------------------------------------------")
        print("Net_Switch script was made by Speed3DBall.")
        time.sleep(2)

def crash():
    print("Something went wrong and script crashed...")
    print("CHECK IF YOU HAVE ADMIN PRIVILEGES.")
    print("RUN THIS SCRIPT AS ADMINISTRATOR ONLY.")
    print("Script was tested on Windows 10.")
    print("------------------------------------------")
    print("Net_Switch script was made by Speed3DBall.")
    time.sleep(15)

ethernet_check()

if 'Disabled' in result.stdout:
    enable_ethernet()

elif 'Enabled' in result.stdout:
    disable_ethernet()

else:
    crash()
