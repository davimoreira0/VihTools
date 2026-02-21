#WIFITE


import os
from colorama import Fore, Style
import time
import subprocess
texto_vihtools = r"""
 ██▒   █▓ ██▓ ██░ ██ ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██░   █▒▓██▒▓██░ ██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒     ▒██    ▒ 
 ▓██  █▒░▒██▒▒██▀▀██░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░     ░ ▓██▄   
  ▒██ █░░░██░░▓█ ░██ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ▒   ██▒
   ▒▀█░  ░██░░▓█▒░██▓  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
   ░ ▐░  ░▓   ▒ ░░▒░▒  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
   ░ ░░   ▒ ░ ▒ ░▒░ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
     ░░   ▒ ░ ░  ░░ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
      ░   ░   ░  ░  ░             ░ ░      ░ ░      ░  ░      ░  
"""

def wifite():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "Hacking Winreless - Wifite" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Wifite:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Crackear redes" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_wifite = input(Fore.RED + "Digite o número do recurso que deseja utilizar: " + Style.RESET_ALL)

    def crackear_redes():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        print(Fore.WHITE + "Iniciando Wifite..." + Style.RESET_ALL)
        time.sleep(1)

        os.system('sudo wifite')

        user_menu = input(Fore.RED + "Voltar para o menu do Wifite (s/n): ")

        if user_menu.lower() == "s":
            wifite()
        else:
            print(Fore.RED + "Saindo do Wifite..." + Style.RESET_ALL)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
        
    if user_wifite.lower() == "1":
        crackear_redes()
    elif user_wifite.lower() == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        wifite()

wifite()