import os
import sys
import time



dirExist = os.path.exists('./torghost')
if dirExist == False:
    os.system('git clone https://github.com/susmithHCK/torghost.git')
    os.system('cd torghost/')
    os.system('chmod +x torghost/install.sh')
    os.system('torghost/./install.sh')
    userTimer = int(input('Enter timer between ip change :  '))
    t = userTimer
    print('Starting Tor Bouncing')
    time.sleep(3)
    os.system('torghost start')
    while(True):
        os.system('torghost switch')
        time.sleep(t)

if dirExist == True:
    userTimer = int(input('Enter timer between ip change :  '))
    t = userTimer
    print('Starting Tor Bouncing')
    time.sleep(3)
    os.system('torghost start')
    while(True):
        os.system('torghost switch')
        time.sleep(t)
