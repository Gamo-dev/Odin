import discord
import os
import ultrarequests
import colorama
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()


colorama.init()
dm = discord.Client()

def clear():
    os.system("title Odin Tool")
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

print(colorama.Fore.RED + '''
████████▄    ▄▄▄▄███▄▄▄▄           ▄████████  ▄█        ▄█            
███   ▀███ ▄██▀▀▀███▀▀▀██▄        ███    ███ ███       ███            
███    ███ ███   ███   ███        ███    ███ ███       ███            
███    ███ ███   ███   ███        ███    ███ ███       ███            
███    ███ ███   ███   ███      ▀███████████ ███       ███            
███    ███ ███   ███   ███        ███    ███ ███       ███            
███   ▄███ ███   ███   ███        ███    ███ ███▌    ▄ ███▌    ▄      
████████▀   ▀█   ███   █▀         ███    █▀  █████▄▄██ █████▄▄██      
                                             ▀         ▀              
  '''
)

token = input("token>>")
message = input("le message que tu veux envoyé>>")
clear()

@dm.event
async def on_connect():
  print("Connecté en tant que :")
  print(dm.user.name)
  print(dm.user.id)
  time.sleep(2)
  clear()

  print("LOADING...")
  time.sleep(0.5)
  clear()
  print(".")
  time.sleep(0.4)
  clear()
  print("..")
  time.sleep(0.4)
  clear()
  print("...")
  time.sleep(0.4)
  clear()

  toaster.show_toast("Odin Tool",
                    "[+] Success now lets dm all friends",
                    duration=4,
                    icon_path = "ico.ico",
                    threaded = True,
                  )

  for user in dm.user.friends:
    try:

      await user.send(message)

      print(f"message envoyé à : {user.name}")
    except:
      print(f"erreur dans l'envoie du message pour : {user.name}")
  print(f"{dm.user.name} tous les utilisateurs ont été dm!")

dm.run(token, bot=False)
