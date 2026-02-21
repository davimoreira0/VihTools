#WHOIS
import os
import time
from colorama import Fore, Style
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
def whois():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: RECONHECIMENTO (RECONNAISSANCE) - WHOIS" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Whois:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Realizar consulta Whois" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_whois = input(Fore.RED + "Selecione uma opção pelo número correspondente: " + Style.RESET_ALL)

    def consulta_whois():
        dominio = input(Fore.RED + "Digite o domínio para consulta Whois: " + Style.RESET_ALL)
        os.system(f'sudo whois {dominio}')

        user_menu = input(Fore.RED + "Deseja voltar ao menu anterior? (s/n): " + Style.RESET_ALL)
        if user_menu.lower() == "s":
            whois()
        else:
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

    if user_whois == "1":
        consulta_whois()
    elif user_whois == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        whois()

whois()