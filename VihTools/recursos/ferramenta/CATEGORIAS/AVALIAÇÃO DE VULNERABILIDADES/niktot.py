#NIKTO
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
def nikto():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: AVALIAÇÃO DE VULNERABILIDADES (VULNERABILITY ASSESSMENT) - NIKTO" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Nikto:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Varredura de vulnerabilidades em servidores web" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar para o menu de avaliação de vulnerabilidades" + Style.RESET_ALL)

    user_recursos_nikto = input(Fore.RED + "Selecione um recurso pelo número correspondente: " + Style.RESET_ALL)

    def varredura_de_vulnerabilidades_em_servidores_web():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_varredura_de_vulnerabilidades_em_servidores_web = input(Fore.RED + "Digite o endereço IP ou domínio para varredura de vulnerabilidades em servidores web: " + Style.RESET_ALL)
        os.system(f'sudo nikto -h {user_varredura_de_vulnerabilidades_em_servidores_web}')

        #voltar para o menu de recursos do nikto
        user_menu_recursos_nikto = input(Fore.RED + "Deseja voltar para o menu de recursos do Nikto? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_nikto.lower() == "s":
            os.system('clear')
            nikto()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)


    if user_recursos_nikto == "1":
        varredura_de_vulnerabilidades_em_servidores_web()
    elif user_recursos_nikto == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        nikto()
        time.sleep(1)

nikto()

