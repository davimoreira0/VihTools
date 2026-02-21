#WPSCAN
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
def wpscant():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: TESTE DE APLICAÇÕES WEB (WEB APPLICATION TESTING) - WPSCAN" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do WPSCAN:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Verificar vulnerabilidades em um site WordPress" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_wpscan = input(Fore.RED + "Selecione uma opção pelo número correspondente: " + Style.RESET_ALL)

    def verificar_vulnerabilidades():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        print(Fore.WHITE + "CATEGORIA: TESTE DE APLICAÇÕES WEB (WEB APPLICATION TESTING) - WPSCAN" + Style.RESET_ALL)
        print(Fore.WHITE + "Opção selecionada: Verificar vulnerabilidades em um site WordPress" + Style.RESET_ALL)
        url = input(Fore.RED + "Digite a URL do site WordPress que deseja verificar: " + Style.RESET_ALL)
        print(Fore.WHITE + f"Verificando vulnerabilidades no site {url}..." + Style.RESET_ALL)
        time.sleep(2)
        os.system(f'wpscan --url {url} --enumerate vp,vt,cb,dbe,u,m --random-user-agent')
        print(Fore.WHITE + "Verificação concluída." + Style.RESET_ALL)

        user_menu = input(Fore.RED + "Deseja realizar outra verificação? (s/n): " + Style.RESET_ALL)
        if user_menu.lower() == "s":
            wpscant()
        else:
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

    if user_wpscan == "1":
        verificar_vulnerabilidades()
    elif user_wpscan == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        wpscant()
        time.sleep(1)

wpscant()