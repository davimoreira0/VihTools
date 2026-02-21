#TCPDUMP
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
def tcpdump():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: ANÁLISE DE TRÁFEGO DE REDE - TCPDUMP" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Tcpdump:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Monitorar todo o tráfego de um IP específico (Host)" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Filtrar tráfego por uma porta específica" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Salvar a captura para analisar no Wireshark (PCAP)" + Style.RESET_ALL)
    print(Fore.WHITE + "[4] Inspecionar o conteúdo dos pacotes em texto puro (ASCII)" + Style.RESET_ALL)
    print(Fore.WHITE + "[5] Combinar múltiplos filtros (Operadores Lógicos)" + Style.RESET_ALL)
    print(Fore.WHITE + "[6] Voltar" + Style.RESET_ALL)

    user_tcpdump_escolha = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)

    def monitorar_ip_host():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        ip_alvo_monitoramento = input(Fore.RED + "Digite o IP da máquina alvo: " + Style.RESET_ALL)
        os.system(f'sudo tcpdump -nn host {ip_alvo_monitoramento}')

        user_menu_recursos_tcpdump = input(Fore.RED + "Deseja voltar para o menu de recursos do Tcpdump? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_tcpdump.lower() == "s":
            os.system('clear')
            tcpdump()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def filtrar_trafego_porta():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        porta_filtro = input(Fore.RED + "Digite a porta específica: " + Style.RESET_ALL)
        os.system(f'sudo tcpdump -nn port {porta_filtro}')
        user_menu_recursos_tcpdump = input(Fore.RED + "Deseja voltar para o menu de recursos do Tcpdump? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_tcpdump.lower() == "s":
            os.system('clear')
            tcpdump()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)
    
    def salvar_captura_pcap():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        placa_wifi = input(Fore.RED + "Digite a sua placa de internet: " + Style.RESET_ALL)
        os.system(f'sudo tcpdump -i {placa_wifi} -s 0 -w captura_rede.pcap')
        user_menu_recursos_tcpdump = input(Fore.RED + "Deseja voltar para o menu de recursos do Tcpdump? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_tcpdump.lower() == "s":
            os.system('clear')
            tcpdump()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def inspecionar_conteudo_ascii():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        os.system(f"sudo tcpdump -A -s 0 'tcp port 80'")
        user_menu_recursos_tcpdump = input(Fore.RED + "Deseja voltar para o menu de recursos do Tcpdump? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_tcpdump.lower() == "s":
            os.system('clear')
            tcpdump()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def combinar_filtros():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        ip_alvo_combinar_filtro = input(Fore.RED + "Digite o IP da máquina alvo: " + Style.RESET_ALL)
        os.system(f'sudo tcpdump -nn src {ip_alvo_combinar_filtro} and dst port 22')
        user_menu_recursos_tcpdump = input(Fore.RED + "Deseja voltar para o menu de recursos do Tcpdump? (s/n): " + Style.RESET_ALL)
        if user_menu_recursos_tcpdump.lower() == "s":
            os.system('clear')
            tcpdump()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def voltar():
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

    if user_tcpdump_escolha == "1":
        monitorar_ip_host()
    elif user_tcpdump_escolha == "2":
        filtrar_trafego_porta()
    elif user_tcpdump_escolha == "3":
        salvar_captura_pcap()
    elif user_tcpdump_escolha == "4":
        inspecionar_conteudo_ascii()
    elif user_tcpdump_escolha == "5":
        combinar_filtros()
    elif user_tcpdump_escolha == "6":
        voltar()
    else:
        tcpdump()
    



    







tcpdump()