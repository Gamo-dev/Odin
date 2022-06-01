# coding: utf-8
import requests
import time
import sys
import subprocess
import os
import colorama

def clear():
    os.system("title Odin Tool")
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

while True:
    
    email = str(input("Entrez votre email[>] "))
    password = str(input("Entrez votre mot de passe[>] "))

    cred = {     
                "email": email,
                "password": password
              }

    r = requests.post('https://discord.com/api/v8/auth/login', json=cred).json()
    if "captcha_key" in r:
        print("Une erreur est survenue. Réécrivez vos informations")
        print(r)
        time.sleep(1)
    elif "errors" in r:
        print("Une erreur est survenue. Réécrivez vos informations.")
        print(r)
    elif r["token"] == None:
        break
    else:
        print("Voici votre token: " + r["token"])
        time.sleep(5)
        sys.exit()

while True:
    if r["token"] == None:
        print("-----------Vérification A2F-----------")
        code = input("Entrez le code d'authentification de l'A2F: ")
        a2f = {
                        "code": code,
                        "ticket": r["ticket"]
                      }
        r2 = requests.post('https://discord.com/api/v8/auth/mfa/totp', json=a2f).json()
        if "message" in r2:
            print("Le code d'authentification A2F est incorrect. Réécrivez le code.")
            time.sleep(1)
        else:
            print("""
░▀█▀░█▀█░█░█░█▀▀░█▀█
░░█░░█░█░█▀▄░█▀▀░█░█
░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀""")
            print("Voici votre token: " + r2["token"])
            time.sleep(5)
            sys.exit()