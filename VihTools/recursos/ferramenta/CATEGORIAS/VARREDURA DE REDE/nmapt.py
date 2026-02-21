#NMAP
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
def funcoes_nmap():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: VARREDURA DE REDE (NETWORK SCANNING) - NMAP" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Nmap:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Varredura de portas (Port Scanning)" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Detecção de sistema operacional (OS Detection)" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Detecção de serviços (Service Detection)" + Style.RESET_ALL)
    print(Fore.WHITE + "[4] Varredura de vulnerabilidades (Vulnerability Scanning)" + Style.RESET_ALL)
    print(Fore.WHITE + "[5] Voltar para o menu principal" + Style.RESET_ALL)

    user_funcoes_nmap = input(Fore.RED + "Selecione um recurso pelo número correspondente: " + Style.RESET_ALL)
    
    #varredura de portas
    def varredura_de_portas():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_varredura_de_portas = input(Fore.RED + "Digite o endereço IP ou domínio para varredura de portas: " + Style.RESET_ALL)
        os.system(f'sudo nmap -p- {user_varredura_de_portas}')

        #voltar para o menu de recursos do nmap
        user_menu_recursos_nmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Nmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_nmap.lower() == "s":
            os.system('clear')
            funcoes_nmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)


    #detecção de sistema operacional
    def deteccao_de_sistema_operacional():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_deteccao_de_sistema_operacional = input(Fore.RED + "Digite o endereço IP ou domínio para detecção de sistema operacional: " + Style.RESET_ALL)
        os.system(f'sudo nmap -O {user_deteccao_de_sistema_operacional}')

        #voltar para o menu de recursos do nmap
        user_menu_recursos_nmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Nmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_nmap.lower() == "s":
            os.system('clear')
            funcoes_nmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    #detecção de serviços
    def deteccao_de_servicos():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_deteccao_de_servicos = input(Fore.RED + "Digite o endereço IP ou domínio para detecção de serviços: " + Style.RESET_ALL)
        os.system(f'sudo nmap -sV {user_deteccao_de_servicos}')

        #voltar para o menu de recursos do nmap
        user_menu_recursos_nmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Nmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_nmap.lower() == "s":
            os.system('clear')
            funcoes_nmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    #varredura de vulnerabilidades
    def varredura_de_vulnerabilidades():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_varredura_de_vulnerabilidades = input(Fore.RED + "Digite o endereço IP ou domínio para varredura de vulnerabilidades: " + Style.RESET_ALL)
        os.system(f'sudo nmap --script vuln {user_varredura_de_vulnerabilidades}')

        #voltar para o menu de recursos do nmap
        user_menu_recursos_nmap = input(Fore.RED + "Deseja voltar para o menu de recursos do Nmap? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_nmap.lower() == "s":
            os.system('clear')
            funcoes_nmap()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)


    if user_funcoes_nmap == "1":
        varredura_de_portas()
    elif user_funcoes_nmap == "2":
        deteccao_de_sistema_operacional()
    elif user_funcoes_nmap == "3":
        deteccao_de_servicos()
    elif user_funcoes_nmap == "4":
        varredura_de_vulnerabilidades()
    elif user_funcoes_nmap == "5":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        os.system('python3 recursos/ferramenta/CATEGORIAS/VARREDURA\ DE\ REDE/nmapt.py')

funcoes_nmap()

