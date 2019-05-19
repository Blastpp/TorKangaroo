import os
import sys
import time
import signal 
import threading
import requests

#From Section

from termcolor import colored, cprint

# Script Starting



#trying to add KeyboardInterrupt

def sigint_handler(signal, frame):
    print('   You pressed Ctrl+C!')
    time.sleep(3)
    print('Turn off TorGhost...')
    time.sleep(3)
    os.system('torghost stop')
    os.system('clear')
    print('And you are back on your public IP:  ')
    print(requests.get('http://ip.42.pl/raw').text)
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

#Does TorGhost path exist?
dirExist = os.path.exists('./torghost')
if dirExist == False:   #If not, Downloading and Installing it.
    os.system('git clone https://github.com/susmithHCK/torghost.git')
    os.system('cd torghost/')
    os.system('chmod +x torghost/install.sh')
    os.system('torghost/./install.sh')
    os.system('clear')

    # Setting Timer Value (In second)
    userTimer = int(input('Enter [In seconds] timer between ip change [Min: 20] :  ')) 
    t = userTimer

    # Starting The Engine..
    print('Starting Tor Bouncing')
    time.sleep(3)
    os.system('torghost start')
    while(True):
        os.system('torghost switch')
        time.sleep(t)

# If TorGhost Directory exist, Just start the engine.

if dirExist == True:


    userTimer = int(input('Enter [In seconds] timer between ip change [Min: 20] :  '))
    t = userTimer

    print('Starting Tor Bouncing')
    time.sleep(3)

    os.system('torghost start')

    while(True):
        os.system('torghost switch')
        time.sleep(t)

