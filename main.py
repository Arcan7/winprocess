import subprocess

# Title: Windows Process
# Description: This is a python script to disable and enable windows update and windows defender
# Version: 1.0.0
# Author: @Anna-el
# Licence: MIT
# Language: Python
# Github: https://github.com/Arcan7
# email: aerabenadrasana@gmail.com

def disable_windows_update():
    subprocess.call('netsh advfirewall set allprofiles state off', shell=True)
    subprocess.call('sc config wuauserv start= disabled', shell=True)

def enable_windows_update():
    subprocess.call('netsh advfirewall set allprofiles state on', shell=True)
    subprocess.call('sc config wuauserv start= auto', shell=True)

def disable_windows_defender():
    subprocess.call('sc config WinDefend start= disabled', shell=True)
    subprocess.call('sc stop WinDefend', shell=True)

def enable_windows_defender():
    subprocess.call('sc config WinDefend start= auto', shell=True)
    subprocess.call('sc start WinDefend', shell=True)

print("-------------------------------------Bonjour et bienvenue dans mon script winprocess-------------------------------------")
print("""
                                                    Nom du script: winprocess
                                                    
      Description: Ce script vous permet de désactiver et d'activer windows update et windows defender
      Auteur: @Anna-el
      Email: aerabenandrasana@gmail.com
      Github: https://github.com/Arcan7
      """)


while True:
    print("1. Activez windows update\n2. Desactivez windows update\n3. Activez windows defender\n4. Desactivez windows defender\n5. Quitter")
    choix = input("Que voulez-vous faire? : ")
    
    if choix == "1":
        enable_windows_update()
        print("Windows update est activé\n")
    elif choix == "2":
        disable_windows_update()
        print("Windows update est désactivé\n")
    elif choix == "3":
        enable_windows_defender()
        print("Windows defender est activé\n")
    elif choix == "4":
        disable_windows_defender()
        print("Windows defender est désactivé\n")
    elif choix == "5":
        print("\nMerci d'avoir utilisé ce script, à bientôt...!!!\n")
        break
    else:
        print("\n\u2192Veuillez entrer une valeur valide\n")
        