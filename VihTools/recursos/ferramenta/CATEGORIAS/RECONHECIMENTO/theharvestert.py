#THEHARVESTER
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
def theharvester():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: RECONHECIMENTO (RECONNAISSANCE) - THEHARVESTER" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do TheHarvester:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Coletar informações de um domínio específico" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Coletar informações de um domínio específico usando uma fonte específica" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Voltar" + Style.RESET_ALL)

    user_theharvester = input(Fore.RED + "Selecione um recurso pelo número correspondente: " + Style.RESET_ALL)

    def coletar_informacoes_dominio():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        print(Fore.WHITE + "CATEGORIA: RECONHECIMENTO (RECONNAISSANCE) - THEHARVESTER" + Style.RESET_ALL)
        print(Fore.WHITE + "Coletar informações de um domínio específico" + Style.RESET_ALL)
        dominio = input(Fore.RED + "Digite o domínio que deseja coletar informações: " + Style.RESET_ALL)
        os.system(f'theharvester -d {dominio} -b all')
        input(Fore.RED + "Pressione Enter para voltar ao menu anterior..." + Style.RESET_ALL)
        theharvester()

    def coletar_informacoes_dominio_fonte():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        print(Fore.WHITE + "CATEGORIA: RECONHECIMENTO (RECONNAISSANCE) - THEHARVESTER" + Style.RESET_ALL)
        print(Fore.WHITE + "Coletar informações de um domínio específico usando uma fonte específica" + Style.RESET_ALL)
        dominio = input(Fore.RED + "Digite o domínio que deseja coletar informações: " + Style.RESET_ALL)
        fonte = input(Fore.RED + "Digite a fonte que deseja usar (ex: google, bing, linkedin, etc): " + Style.RESET_ALL)
        os.system(f'theharvester -d {dominio} -b {fonte}')
        
        user_menu = input(Fore.RED + "Deseja voltar ao menu anterior? (s/n): " + Style.RESET_ALL)
        if user_menu.lower() == "s":
            theharvester()
        else:
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

    if user_theharvester == "1":
        coletar_informacoes_dominio()
    elif user_theharvester == "2":
        coletar_informacoes_dominio_fonte()
    elif user_theharvester == "3":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        theharvester()
        time.sleep(1)

theharvester()

