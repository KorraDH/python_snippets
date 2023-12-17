#Esercizio 016 di https://www.programmareinpython.it/esercizi-python/

import platform

print("Sistema operativo: " + str(platform.system()))

print("Kernel: " + str(platform.release()))

print("Il processore ha architettura: " + str(platform.processor()))

#info per installazione linux

if platform.system() == "Linux":
    release = {}
    release = platform.freedesktop_os_release()
    #print(platform.freedesktop_os_release()) 
    print( str(platform.system()) + " " + str(release["PRETTY_NAME"]) + " - codename: " + str(release["VERSION_CODENAME"]))