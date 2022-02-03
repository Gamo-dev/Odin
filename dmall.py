import discord
import os
import colorama
import time

colorama.init()
dm = discord.Client()

def clear():
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

  for user in dm.user.friends:
    try:

      await user.send(message)

      print(f"message envoyé à : {user.name}")
    except:
      print(f"erreur dans l'envoie du message pour : {user.name}")
  print(f"{dm.user.name} tous les utilisateurs ont été dm!")

dm.run(token, bot=False)
