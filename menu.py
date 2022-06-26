import requests
import time
import sys
import subprocess
import os
import ascii2text
import discord
import colorama
from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast("Odin Tool",
                   "[+] READY to dm mass people !",
                   duration=4,
                   icon_path = "ico.ico",
    			   threaded = True,
    			)

colorama.init()

def clear():
    os.system("title Odin Tool")
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def main():
	clear()
	print(colorama.Fore.RED + """
 ▒█████  ▓█████▄  ██▓ ███▄    █    
▒██▒  ██▒▒██▀ ██▌▓██▒ ██ ▀█   █    
▒██░  ██▒░██   █▌▒██▒▓██  ▀█ ██▒   
▒██   ██░░▓█▄   ▌░██░▓██▒  ▐▌██▒   
░ ████▓▒░░▒████▓ ░██░▒██░   ▓██░   
░ ▒░▒░▒░  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒    
  ░ ▒ ▒░  ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░   
░ ░ ░ ▒   ░ ░  ░  ▒ ░   ░   ░ ░    
    ░ ░     ░     ░           ░    
          ░                        """)

	print(colorama.Fore.RED +"dont forget to install requirements.txt")

	menu = input(colorama.Fore.BLUE +"\n\n [1]-get token of your account\n\n [2]-dm all of your friends\n\nplease enter a number[>]")

	if menu == '1':
		clear()
		gettoken()
	if menu == '2':
		clear()
		dmall()

	else:
		clear()
		main()

def dmall():
	clear()
	os.system("python dmall.py")

def gettoken():
	clear()
	os.system("python gettoken.py")

if __name__ == "__main__":
    main()