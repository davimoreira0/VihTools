#ZPHISHER
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

def zphisher():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "Engenharia social - Zphisher" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Zphisher:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Inciar Zphisher" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_zphisher = input(Fore.RED + "Digite o número do recurso que deseja utilizar: " + Style.RESET_ALL)

    def iniciar_zphisher():
        os.system("bash  zphisher/zphisher.sh")

        user_menu = input(Fore.RED + "Voltar para o menu do Zphisher (s/n): ")

        if user_menu.lower() == "s":
            zphisher()
        else:
            print(Fore.RED + "Saindo do Zphisher..." + Style.RESET_ALL)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

    if user_zphisher.lower() == "1":
        iniciar_zphisher()
    elif user_zphisher.lower() == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        zphisher()
    
zphisher()

